import os
from typing import Iterable, List, Optional

from langchain_core.documents import Document
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

from project.services.metric_knowledge import METRICS_DB
from project.data.scientific_corpus import SCIENTIFIC_CORPUS

# FastEmbed cache directory (avoids repeated downloads)
_CACHE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..", ".cache", "fastembed")
)
_EMBEDDING_DIMENSIONS = 384


def _build_embeddings() -> FastEmbedEmbeddings:
    """
    Build FastEmbed embeddings (ONNX backend, no PyTorch needed).
    Uses all-MiniLM-L6-v2 compiled to ONNX for fast startup (~1-2s vs 23s).
    """
    return FastEmbedEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        cache_dir=_CACHE_DIR,
    )


class KnowledgeIndexer:
    """
    Ingestion pipeline for the project's curated scientific knowledge.

    The indexer only loads records already present in the repository. It does
    not fetch web pages or ask an LLM to create scientific content.
    """

    def __init__(
        self,
        collection_name: str = "scientific_knowledge",
        url: Optional[str] = None,
        client: Optional[QdrantClient] = None,
        chunk_size: int = 700,
        chunk_overlap: int = 100,
    ):
        self.collection_name = collection_name
        self.embeddings = _build_embeddings()
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        self.client = client or (QdrantClient(url=url) if url else QdrantClient(location=":memory:"))
        self._ensure_collection()

        self.vector_store = QdrantVectorStore(
            client=self.client,
            collection_name=self.collection_name,
            embedding=self.embeddings,
        )

    def _ensure_collection(self) -> None:
        if not self.client.collection_exists(self.collection_name):
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(size=_EMBEDDING_DIMENSIONS, distance=Distance.COSINE),
            )

    def load_scientific_documents(self) -> List[Document]:
        """Load curated scientific records from the metrics database and evidence corpus."""
        return self.load_metrics_as_documents() + self.load_corpus_as_documents()

    def load_metrics_as_documents(self) -> List[Document]:
        """Convert METRICS_DB into LangChain Documents with preserved metadata."""
        documents: List[Document] = []

        for metric in METRICS_DB:
            content = (
                f"Metric: {metric.name}\n"
                f"Domain: {metric.domain.value}\n"
                f"Description: {metric.description}\n"
                f"Why it matters: {metric.why_it_matters}\n"
                f"Problems investigated: {', '.join(metric.problems_investigated)}\n"
                f"Related variables: {', '.join(metric.related_variables)}\n"
                f"Measurement unit: {metric.measurement_unit}\n"
                f"Scientific source: {metric.source.organization} - {metric.source.evidence_provenance}"
            )

            metadata = {
                "source": metric.source.source_id,
                "organization": metric.source.organization,
                "title": f"{metric.name} metric metadata",
                "URL": metric.source.url or "",
                "url": metric.source.url or "",
                "domain": metric.domain.value,
                "document type": "Environmental Metric",
                "document_type": "Environmental Metric",
                "metric": metric.name,
                "evidence type": metric.source.evidence_provenance,
                "evidence_type": metric.source.evidence_provenance,
                "measurement_unit": metric.measurement_unit,
                "knowledge_origin": "curated_project_metric_database",
            }

            documents.append(Document(page_content=content, metadata=metadata))

        return documents

    def load_corpus_as_documents(self) -> List[Document]:
        """Convert SCIENTIFIC_CORPUS evidence passages into LangChain Documents with preserved metadata."""
        documents: List[Document] = []

        for entry in SCIENTIFIC_CORPUS:
            metadata = {
                "source": entry["source_id"],
                "organization": entry["organization"],
                "title": entry["evidence_provenance"],
                "URL": entry["url"],
                "url": entry["url"],
                "document_type": entry["document_type"],
                "document type": entry["document_type"],
                "evidence_type": entry["evidence_provenance"],
                "evidence type": entry["evidence_provenance"],
                "topic_tags": ", ".join(entry.get("topic_tags", [])),
                "knowledge_origin": "curated_scientific_corpus",
            }
            documents.append(Document(page_content=entry["content"], metadata=metadata))

        return documents

    def split_documents(self, documents: Iterable[Document]) -> List[Document]:
        """Split scientific documents into retrieval-friendly chunks."""
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=["\n\n", "\n", ". ", ", ", " "],
        )
        return splitter.split_documents(list(documents))

    def index_documents(self, documents: Iterable[Document]) -> List[str]:
        """Generate embeddings and store document chunks in Qdrant."""
        return self.vector_store.add_documents(list(documents))

    def ingest(self) -> List[str]:
        """Run the complete ingestion pipeline against the curated project knowledge."""
        raw_documents = self.load_scientific_documents()
        split_documents = self.split_documents(raw_documents)
        return self.index_documents(split_documents)


class KnowledgeRetriever:
    """
    Semantic retrieval from Qdrant.

    Retrieval returns source documents and metadata directly. Downstream LLM
    features should consume these results as evidence, not as generated facts.
    """

    def __init__(self, vector_store: QdrantVectorStore, default_k: int = 3):
        self.vector_store = vector_store
        self.default_k = default_k

    def retrieve(self, query: str, k: int = 3) -> List[Document]:
        results = self.retrieve_with_scores(query, k=k)
        return [document for document, _score in results]

    def retrieve_with_scores(self, query: str, k: Optional[int] = None) -> List[tuple[Document, float]]:
        """Return semantically similar scientific chunks with Qdrant relevance scores."""
        search_k = k or self.default_k
        results = self.vector_store.similarity_search_with_score(query, k=search_k)

        scored_documents: List[tuple[Document, float]] = []
        for document, score in results:
            document.metadata = {
                **document.metadata,
                "relevance_score": score,
            }
            scored_documents.append((document, score))

        return scored_documents
