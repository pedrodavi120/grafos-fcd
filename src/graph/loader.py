# script para carregar os dados no neo4j usando unwind e merge
import sys
from pathlib import Path
import pandas as pd

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from src.config import PROCESSED_DATA_DIR
from src.graph.connection import Neo4jManager
from src.graph.schema import apply_schema

# query para criar os nos de componentes sem duplicar
QUERY_INGEST_NODES = """
UNWIND $batch AS comp
MERGE (c:Componente {codigo: comp.codigo})
SET c.nome = comp.nome,
    c.ch = toInteger(comp.ch),
    c.semestre = toInteger(comp.semestre),
    c.natureza = comp.natureza,
    c.area = comp.area
RETURN count(c) AS total_inseridos;
"""

# query para conectar as disciplinas pelas arestas de pre-requisito
QUERY_INGEST_EDGES = """
UNWIND $relacoes AS rel
MATCH (origem:Componente {codigo: rel.codigo_origem})
MATCH (destino:Componente {codigo: rel.codigo_destino})
MERGE (origem)-[r:E_PRE_REQUISITO_DE]->(destino)
RETURN count(r) AS total_arestas;
"""


def load_graph(manager: Neo4jManager) -> dict:
    # carrega os csvs e manda pro banco
    nodes_file = PROCESSED_DATA_DIR / "nodes_componentes.csv"
    edges_file = PROCESSED_DATA_DIR / "edges_prerequisitos.csv"

    if not nodes_file.exists() or not edges_file.exists():
        raise FileNotFoundError("arquivos processados nao encontrados, rode o make_dataset primeiro")

    df_nodes = pd.read_csv(nodes_file)
    df_edges = pd.read_csv(edges_file)

    records_nodes = df_nodes.to_dict(orient="records")
    records_edges = df_edges.to_dict(orient="records")

    driver = manager.get_driver()

    with driver.session(database=manager.database) as session:
        # cria indices e constraints
        apply_schema(session)

        # insere nos
        res_nodes = session.run(QUERY_INGEST_NODES, batch=records_nodes)
        total_nodes = res_nodes.single()["total_inseridos"]

        # insere arestas
        res_edges = session.run(QUERY_INGEST_EDGES, relacoes=records_edges)
        total_edges = res_edges.single()["total_arestas"]

    return {
        "status": "success",
        "nodes_loaded": total_nodes,
        "edges_loaded": total_edges
    }


def main():
    print("iniciando carga de dados no neo4j...")
    manager = Neo4jManager()

    print(f"conectando em {manager.uri}...")
    if not manager.check_connection():
        print("neo4j nao esta acessivel agora. suba o banco local ou configure o auradb no .env")
        sys.exit(1)

    res = load_graph(manager)
    print("carga finalizada:")
    print(f"nos criados: {res['nodes_loaded']}")
    print(f"arestas criadas: {res['edges_loaded']}")
    manager.close()


if __name__ == "__main__":
    main()
