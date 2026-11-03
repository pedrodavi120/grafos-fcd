# Interface Web Opcional (PoC com Streamlit)
# Conforme abordado nas aulas do Prof. Josenalde ("UI rápida para PoC - STREAMLIT")
import streamlit as st
import pandas as pd
from pathlib import Path
import networkx as nx

from src.config import PROCESSED_DATA_DIR, FIGURES_DIR
from src.analysis.graph_metrics import load_graph_from_processed, calculate_centralities, find_critical_paths, get_k_hop_successors

st.set_page_config(
    page_title="Validação Neo4j - TADS/UFRN",
    layout="wide"
)

st.title("Validação Tecnológica: Bases de Dados em Grafos (Neo4j & Cypher)")
st.caption("Disciplina: Fundamentos e Técnicas em Ciência de Dados — TADS / EAJ - UFRN (Prof. Josenalde Oliveira)")
st.write("Equipe: Pedro Davi, Cleiton Mizael e Natanael Lucas")

st.markdown("---")

# Carregar grafo e metricas
G = load_graph_from_processed()
df_metrics = calculate_centralities(G)

# Linha de metricas principais (KPIs)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Componentes Curriculares", G.number_of_nodes())
col2.metric("Relações de Pré-Requisito", G.number_of_edges())
col3.metric("Estrutura da Rede", "DAG (Acíclico)" if nx.is_directed_acyclic_graph(G) else "Com Ciclos")
critical_len, critical_path = find_critical_paths(G)[0]
col4.metric("Caminho Crítico", f"{critical_len} Semestres")

st.markdown("---")

# Abas de exploracao
tab1, tab2, tab3 = st.tabs(["Consulta de Disciplina (k-hop)", "Métricas de Rede e Gargalos", "Figuras Analíticas"])

with tab1:
    st.subheader("Simulação de Travessia Cypher por Salto")
    disciplinas_dict = {f"{row['codigo']} - {row['nome']}": row['codigo'] for _, row in df_metrics.iterrows()}
    escolha = st.selectbox("Selecione um componente curricular:", list(disciplinas_dict.keys()))
    codigo_sel = disciplinas_dict[escolha]

    # Pre-requisitos exigidos (In-Degree)
    pre_reqs = list(G.predecessors(codigo_sel))
    # Disciplinas que destrava (Out-Degree)
    destrava = list(G.successors(codigo_sel))

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Pré-Requisitos Imediatos Exigidos:**")
        if pre_reqs:
            for p in pre_reqs:
                st.write(f"- `{p}`: {G.nodes[p]['nome']}")
        else:
            st.write("Nenhum pré-requisito (componente de entrada).")

    with c2:
        st.markdown("**Disciplinas Destravadas Diretamente (1 Salto):**")
        if destrava:
            for d in destrava:
                st.write(f"- `{d}`: {G.nodes[d]['nome']}")
        else:
            st.write("Não é pré-requisito direto de nenhum componente.")

    st.markdown("**Cadeia de Travessia Profunda (1 a 3 Saltos a partir deste componente):**")
    try:
        k_hops = get_k_hop_successors(G, codigo_sel, k=3)
        for salto, lista in k_hops.items():
            if lista:
                st.write(f"• **Salto {salto}:** {', '.join([f'{c} ({G.nodes[c][\"nome\"]})' for c in lista])}")
    except Exception as e:
        st.error(f"Erro no percurso: {e}")

with tab2:
    st.subheader("Tabela de Métricas e Centralidades Curriculares")
    st.dataframe(
        df_metrics[["codigo", "nome", "semestre", "ch", "in_degree", "out_degree", "betweenness_centrality"]],
        use_container_width=True
    )
    st.info("Betweenness Centrality indica o grau de intermediação da disciplina (disciplinas gargalo que, se reprovadas, retêm o fluxo de formatura).")

with tab3:
    st.subheader("Figuras Analíticas Exportadas")
    fig_col1, fig_col2 = st.columns(2)
    with fig_col1:
        st.image(str(FIGURES_DIR / "ranking_betweenness_gargalos.png"), caption="Disciplinas Gargalo (Betweenness Centrality)")
    with fig_col2:
        st.image(str(FIGURES_DIR / "grau_centralidade_distribuicao.png"), caption="Dispersão de Pré-Requisitos Exigidos vs Destravados")
    st.image(str(FIGURES_DIR / "topologia_dag_curricular.png"), caption="Topologia Estratificada por Semestre do Curso de TADS")
