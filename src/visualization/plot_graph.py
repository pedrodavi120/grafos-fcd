# script para gerar e salvar os graficos da apresentacao
import sys
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from src.config import FIGURES_DIR
from src.analysis.graph_metrics import load_graph_from_processed, calculate_centralities


def plot_betweenness_ranking(df_metrics, output_path: Path):
    # plota as disciplinas com maior betweenness
    plt.figure(figsize=(10, 6))
    sns.set_theme(style="whitegrid")

    top_df = df_metrics.sort_values(by="betweenness_centrality", ascending=True).tail(8)

    bars = plt.barh(
        top_df["nome"],
        top_df["betweenness_centrality"],
        color="#2b5c8f",
        edgecolor="#1a365d"
    )

    plt.title("Disciplinas Gargalo no Fluxo Curricular (Betweenness Centrality)", fontsize=12, weight="bold")
    plt.xlabel("Betweenness Centrality (Normalizada)")
    plt.ylabel("Componente Curricular")

    for bar in bars:
        width = bar.get_width()
        if width > 0:
            plt.text(width + 0.0003, bar.get_y() + bar.get_height() / 2, f"{width:.4f}",
                     ha="left", va="center", fontsize=9, color="#333333")

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"figura salva em {output_path}")


def plot_degrees_scatter(df_metrics, output_path: Path):
    # dispersao entre grau de entrada e grau de saida
    plt.figure(figsize=(10, 6))
    sns.set_theme(style="whitegrid")

    ax = sns.scatterplot(
        data=df_metrics,
        x="in_degree",
        y="out_degree",
        size="ch",
        hue="semestre",
        palette="viridis",
        sizes=(80, 260),
        alpha=0.85,
        edgecolor="black"
    )

    plt.title("Relacao entre Pre-Requisitos Exigidos vs Destravados", fontsize=12, weight="bold")
    plt.xlabel("In-Degree (Pre-requisitos que a materia exige)")
    plt.ylabel("Out-Degree (Materias que ela destrava)")

    for _, row in df_metrics.iterrows():
        if row["out_degree"] >= 3 or row["in_degree"] >= 2:
            ax.annotate(
                row["codigo"],
                (row["in_degree"] + 0.08, row["out_degree"] + 0.08),
                fontsize=8,
                weight="bold"
            )

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"figura salva em {output_path}")


def plot_curriculum_dag(G: nx.DiGraph, output_path: Path):
    # renderiza o grafo com as disciplinas organizadas por semestre
    plt.figure(figsize=(14, 8))

    pos = {}
    semestre_counts = {}
    for node, data in G.nodes(data=True):
        sem = data.get("semestre", 1)
        semestre_counts[sem] = semestre_counts.get(sem, 0) + 1

    semestre_current = {}
    for node, data in G.nodes(data=True):
        sem = data.get("semestre", 1)
        idx = semestre_current.get(sem, 0)
        total = semestre_counts[sem]
        y_pos = (idx - total / 2.0) * 1.5
        pos[node] = (sem, y_pos)
        semestre_current[sem] = idx + 1

    nx.draw_networkx_nodes(
        G, pos,
        node_size=800,
        node_color="#3182ce",
        edgecolors="#1a365d",
        linewidths=1.5
    )
    nx.draw_networkx_edges(
        G, pos,
        arrowstyle="-|>",
        arrowsize=14,
        edge_color="#718096",
        width=1.2,
        connectionstyle="arc3,rad=0.1"
    )
    nx.draw_networkx_labels(
        G, pos,
        font_size=8,
        font_family="sans-serif",
        font_weight="bold",
        font_color="#ffffff"
    )

    plt.title("Topologia da Grade de TADS/EAJ (Organizada por Semestre)", fontsize=13, weight="bold")
    plt.xlabel("Semestre")
    plt.xticks(range(1, 7), [f"{i}o Semestre" for i in range(1, 7)])
    plt.yticks([])
    plt.grid(axis="x", linestyle="--", alpha=0.6)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"figura salva em {output_path}")


def main():
    print("gerando graficos para o relatorio...")
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    G = load_graph_from_processed()
    df_metrics = calculate_centralities(G)

    plot_betweenness_ranking(df_metrics, FIGURES_DIR / "ranking_betweenness_gargalos.png")
    plot_degrees_scatter(df_metrics, FIGURES_DIR / "grau_centralidade_distribuicao.png")
    plot_curriculum_dag(G, FIGURES_DIR / "topologia_dag_curricular.png")
    print("graficos gerados com sucesso.")


if __name__ == "__main__":
    main()
