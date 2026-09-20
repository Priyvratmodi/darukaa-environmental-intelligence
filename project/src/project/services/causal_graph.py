import json
import os
from langchain_community.graphs import Neo4jGraph

def get_causal_graph() -> Neo4jGraph:
    """
    Initializes and returns the Neo4j knowledge graph connection.
    """
    neo4j_uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    neo4j_user = os.getenv("NEO4J_USER", "neo4j")
    neo4j_password = os.getenv("NEO4J_PASSWORD", "password")
    
    return Neo4jGraph(url=neo4j_uri, username=neo4j_user, password=neo4j_password)

def load_causal_edges(json_path: str = "data/causal_edges.json") -> None:
    """
    Loads causal edges from the JSON data into the Neo4j knowledge graph.
    Only supports approved nodes and relationships.
    """
    if not os.path.exists(json_path):
        return
        
    graph = get_causal_graph()
    
    with open(json_path, 'r') as f:
        edges = json.load(f)
        
    valid_labels = {
        "Driver", "EnvironmentalMetric", "EnvironmentalState",
        "BiodiversityOutcome", "Species", "Ecosystem", "Intervention"
    }
    
    valid_relations = {
        "CAUSES", "CONTRIBUTES_TO", "INFLUENCES", "AFFECTS"
    }
    
    for edge in edges:
        source_label = edge.get("source_label", "EnvironmentalMetric")
        target_label = edge.get("target_label", "EnvironmentalState")
        relation = edge.get("relation", "INFLUENCES").upper()
        
        # Enforce ontology constraints
        if source_label not in valid_labels or target_label not in valid_labels:
            continue
        if relation not in valid_relations:
            continue
            
        source_name = edge.get("source_name")
        target_name = edge.get("target_name")
        
        if not source_name or not target_name:
            continue
            
        # Store source/provenance information with relationships
        provenance = edge.get("provenance", "")
        source_url = edge.get("source_url", "")
        confidence = edge.get("confidence", 1.0)
        
        query = f"""
        MERGE (s:{source_label} {{name: $source_name}})
        MERGE (t:{target_label} {{name: $target_name}})
        MERGE (s)-[r:{relation}]->(t)
        SET r.provenance = $provenance, 
            r.source_url = $source_url,
            r.confidence = $confidence
        """
        
        graph.query(query, params={
            "source_name": source_name,
            "target_name": target_name,
            "provenance": provenance,
            "source_url": source_url,
            "confidence": confidence
        })
