import pytest
from project.services.qdrant_retrieval import KnowledgeIndexer, KnowledgeRetriever


def test_qdrant_semantic_retrieval():
    # Use memory for reliable, isolated testing without Docker
    indexer = KnowledgeIndexer(url=None)
    indexed_ids = indexer.ingest()
    assert len(indexed_ids) > 0
    
    retriever = KnowledgeRetriever(indexer.vector_store)
    
    queries = [
        "What measurements are needed to investigate soil degradation?",
        "What environmental factors are associated with declining biodiversity?",
        "What factors should be considered when investigating habitat fragmentation?"
    ]
    
    print("\n" + "="*50)
    for query in queries:
        print(f"QUERY\n{query}")
        results = retriever.retrieve_with_scores(query, k=2)
        for document, score in results:
            print(f"RETRIEVED DOCUMENT\n{document.page_content.strip()}")
            print(f"SOURCE\n{document.metadata.get('source')}")
            print(f"RELEVANCE/METADATA\nscore={score}; metadata={document.metadata}")
        print("-" * 50)
        
        assert len(results) > 0, f"Failed to retrieve results for query: {query}"
        
        # Verify metadata preservation
        document = results[0][0]
        assert "source" in document.metadata
        assert "organization" in document.metadata
        assert "title" in document.metadata
        assert "URL" in document.metadata
        assert "domain" in document.metadata
        assert "document type" in document.metadata
        assert "metric" in document.metadata
        assert "evidence type" in document.metadata
        assert "relevance_score" in document.metadata
