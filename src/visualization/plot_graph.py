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
    # plota as disciplinas com maior betweenness com destaque para Ciencia de Dados
    plt.figure(figsize=(11, 6))
    sns.set_theme(style="whitegrid")

    top_df = df_metrics.sort_values(by="betweenness_centrality", ascending=True).tail(8)

    # destaca a disciplina do professor com uma cor diferenciada
    colors = ["#2b5c8f" if "CIENCIA DE DADOS" not in nome else "#10b981" for nome in top_df["nome"]]

    bars = plt.barh(
        top_df["nome"],
        top_df["betweenness_centrality"],
        color=colors,
        edgecolor="#1a365d"
    )

    plt.title("Disciplinas Gargalo no Fluxo Curricular (Betweenness Centrality)", fontsize=13, weight="bold", pad=15)
    plt.xlabel("Betweenness Centrality (Normalizada)", fontsize=11)
    plt.ylabel("Componente Curricular", fontsize=11)

    for bar in bars:
        width = bar.get_width()
        if width > 0:
            plt.text(width + 0.0003, bar.get_y() + bar.get_height() / 2, f"{width:.4f}",
                     ha="left", va="center", fontsize=9, color="#111827", weight="bold")

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"figura salva em {output_path}")


def plot_degrees_scatter(df_metrics, output_path: Path):
    # dispersao entre grau de entrada e grau de saida com legenda externa para nao sobrepor
    plt.figure(figsize=(11, 6))
    sns.set_theme(style="whitegrid")

    ax = sns.scatterplot(
        data=df_metrics,
        x="in_degree",
        y="out_degree",
        size="ch",
        hue="semestre",
        palette="viridis",
        sizes=(100, 300),
        alpha=0.9,
        edgecolor="black"
    )

    plt.title("Relação entre Pré-Requisitos Exigidos vs. Destravados (TADS/EAJ)", fontsize=13, weight="bold", pad=15)
    plt.xlabel("In-Degree (Nº de Pré-Requisitos que a matéria exige)", fontsize=11)
    plt.ylabel("Out-Degree (Nº de Matérias que ela destrava diretamente)", fontsize=11)

    # anota os nós estruturantes de maior relevância
    for _, row in df_metrics.iterrows():
        if row["out_degree"] >= 3 or row["in_degree"] >= 2 or row["codigo"] == "TAD0204":
            offset_y = 0.12 if row["out_degree"] < 4 else -0.18
            ax.annotate(
                f"{row['codigo']}",
                (row["in_degree"] + 0.06, row["out_degree"] + offset_y),
                fontsize=8.5,
                weight="bold",
                color="#1e293b"
            )

    # posiciona legenda fora da area de plotagem para nao cobrir dados
    plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left", borderaxespad=0, title="Atributos")

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"figura salva em {output_path}")


def plot_curriculum_dag(G: nx.DiGraph, output_path: Path):
    # renderiza o grafo com as disciplinas organizadas por semestre
    plt.figure(figsize=(15, 9))

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
        y_pos = (idx - total / 2.0) * 1.6
        pos[node] = (sem, y_pos)
        semestre_current[sem] = idx + 1

    # cores dos nos: verde para FCD (TAD0204), azul padrao para as demais
    node_colors = ["#10b981" if n == "TAD0204" else "#3182ce" for n in G.nodes()]

    nx.draw_networkx_nodes(
        G, pos,
        node_size=1100,
        node_color=node_colors,
        edgecolors="#0f172a",
        linewidths=1.5
    )
    nx.draw_networkx_edges(
        G, pos,
        arrowstyle="-|>",
        arrowsize=12,
        edge_color="#64748b",
        width=1.3,
        connectionstyle="arc3,rad=0.08"
    )
    nx.draw_networkx_labels(
        G, pos,
        font_size=7,
        font_family="sans-serif",
        font_weight="bold",
        font_color="#ffffff"
    )

    plt.title("Topologia da Grade de TADS/EAJ - Matriz 2019.2 (Organizada por Semestre)", fontsize=14, weight="bold", pad=15)
    plt.xlabel("Período Curricular", fontsize=11)
    plt.xticks(range(1, 7), [f"{i}º Nível" for i in range(1, 7)], fontsize=10)
    plt.yticks([])
    plt.grid(axis="x", linestyle="--", alpha=0.6)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"figura salva em {output_path}")


def main():
    print("gerando graficos analiticos de alta resolucao...")
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    G = load_graph_from_processed()
    df_metrics = calculate_centralities(G)

    plot_betweenness_ranking(df_metrics, FIGURES_DIR / "ranking_betweenness_gargalos.png")
    plot_degrees_scatter(df_metrics, FIGURES_DIR / "grau_centralidade_distribuicao.png")
    plot_curriculum_dag(G, FIGURES_DIR / "topologia_dag_curricular.png")
    print("graficos atualizados com sucesso.")


if __name__ == "__main__":
    main()
