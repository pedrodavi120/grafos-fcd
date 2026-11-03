# script para calcular metricas de grafo com networkx
import sys
from pathlib import Path
from typing import Dict, List, Tuple
import pandas as pd
import networkx as nx

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from src.config import PROCESSED_DATA_DIR


def build_networkx_graph(nodes_df: pd.DataFrame, edges_df: pd.DataFrame) -> nx.DiGraph:
    # monta o digrafo direcionado no networkx
    G = nx.DiGraph()

    for _, row in nodes_df.iterrows():
        G.add_node(
            row["codigo"],
            nome=row["nome"],
            ch=int(row["ch"]),
            semestre=int(row["semestre"]),
            natureza=row["natureza"],
            area=row["area"]
        )

    for _, row in edges_df.iterrows():
        G.add_edge(
            row["codigo_origem"],
            row["codigo_destino"],
            tipo=row["tipo_relacao"]
        )

    return G


def load_graph_from_processed() -> nx.DiGraph:
    # le os csvs processados e devolve o grafo
    nodes_file = PROCESSED_DATA_DIR / "nodes_componentes.csv"
    edges_file = PROCESSED_DATA_DIR / "edges_prerequisitos.csv"

    if not nodes_file.exists() or not edges_file.exists():
        raise FileNotFoundError("arquivos processados nao encontrados")

    df_nodes = pd.read_csv(nodes_file)
    df_edges = pd.read_csv(edges_file)
    return build_networkx_graph(df_nodes, df_edges)


def calculate_centralities(G: nx.DiGraph) -> pd.DataFrame:
    # calcula in-degree, out-degree, betweenness e closeness
    in_degrees = dict(G.in_degree())
    out_degrees = dict(G.out_degree())
    betweenness = nx.betweenness_centrality(G, normalized=True)
    closeness = nx.closeness_centrality(G)

    records = []
    for node in G.nodes():
        data = G.nodes[node]
        records.append({
            "codigo": node,
            "nome": data.get("nome", node),
            "semestre": data.get("semestre", 0),
            "area": data.get("area", "N/A"),
            "ch": data.get("ch", 0),
            "in_degree": in_degrees[node],
            "out_degree": out_degrees[node],
            "betweenness_centrality": round(betweenness[node], 4),
            "closeness_centrality": round(closeness[node], 4)
        })

    df = pd.DataFrame(records)
    return df.sort_values(by=["betweenness_centrality", "out_degree"], ascending=False)


def find_critical_paths(G: nx.DiGraph) -> List[Tuple[int, List[str]]]:
    # encontra a maior cadeia de pre-requisitos em saltos
    if not nx.is_directed_acyclic_graph(G):
        raise ValueError("grafo possui ciclos, nao e dag")

    longest_path = nx.dag_longest_path(G)
    longest_len = len(longest_path) - 1
    return [(longest_len, longest_path)]


def get_k_hop_successors(G: nx.DiGraph, source_node: str, k: int = 3) -> Dict[int, List[str]]:
    # retorna quais disciplinas sao alcancadas em 1, 2 ate k saltos
    if source_node not in G:
        raise KeyError(f"disciplina {source_node} nao encontrada no grafo")

    lengths = nx.single_source_shortest_path_length(G, source_node, cutoff=k)
    by_depth: Dict[int, List[str]] = {i: [] for i in range(1, k + 1)}

    for node, depth in lengths.items():
        if depth > 0 and depth <= k:
            by_depth[depth].append(node)

    return by_depth


def main():
    print("calculando metricas do grafo curricular...")
    G = load_graph_from_processed()
    print(f"vertices: {G.number_of_nodes()} | arestas: {G.number_of_edges()}")
    print(f"e um dag (sem ciclos)? {nx.is_directed_acyclic_graph(G)}")

    df_metrics = calculate_centralities(G)
    print("\nprincipais gargalos por betweenness:")
    print(df_metrics[["codigo", "nome", "semestre", "betweenness_centrality", "out_degree"]].head(5).to_string(index=False))

    print("\nmaiores provedores de pre-requisito (out-degree):")
    df_out = df_metrics.sort_values(by="out_degree", ascending=False)
    print(df_out[["codigo", "nome", "out_degree"]].head(5).to_string(index=False))

    critical = find_critical_paths(G)
    length, path = critical[0]
    print(f"\ncaminho critico de formatura ({length} saltos):")
    print(" -> ".join(path))


if __name__ == "__main__":
    main()
