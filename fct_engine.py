import json

def analyze_graph(graph):
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])

    node_count = len(nodes)
    edge_count = len(edges)

    # Anchor detection (simple heuristic)
    anchors = [n for n in nodes if n.get("type") == "anchor"]
    anchor_count = len(anchors)

    # Unsupported edges (no source/citation)
    unsupported_edges = [e for e in edges if not e.get("source")]
    unsupported_ratio = len(unsupported_edges) / edge_count if edge_count else 0

    result = {
        "node_count": node_count,
        "edge_count": edge_count,
        "anchor_count": anchor_count,
        "unsupported_edge_ratio": round(unsupported_ratio, 2),
        "verdict": "Possible FCT" if unsupported_ratio > 0.5 else "Low FCT signal"
    }

    return result
