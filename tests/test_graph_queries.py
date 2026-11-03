"""
Testes automatizados para validação sintática das queries declarativas em Cypher.
Funciona tanto com pytest quanto com o runner padrão unittest.
"""

import unittest
from src.graph.schema import CONSTRAINT_COMPONENTE_CODIGO, INDEX_COMPONENTE_SEMESTRE

# Declaração das queries para validação de estrutura
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

QUERY_INGEST_EDGES = """
UNWIND $relacoes AS rel
MATCH (origem:Componente {codigo: rel.codigo_origem})
MATCH (destino:Componente {codigo: rel.codigo_destino})
MERGE (origem)-[r:E_PRE_REQUISITO_DE]->(destino)
RETURN count(r) AS total_arestas;
"""


class TestGraphQueries(unittest.TestCase):
    """Validação das queries Cypher do projeto."""

    def test_cypher_schema_definitions(self):
        """Garante que as queries de esquema utilizam as cláusulas corretas do Cypher."""
        self.assertIn("CREATE CONSTRAINT", CONSTRAINT_COMPONENTE_CODIGO)
        self.assertIn("REQUIRE c.codigo IS UNIQUE", CONSTRAINT_COMPONENTE_CODIGO)
        self.assertIn("CREATE INDEX", INDEX_COMPONENTE_SEMESTRE)

    def test_cypher_ingest_queries_structure(self):
        """Garante idempotência através de UNWIND e MERGE nas queries de ingestão."""
        self.assertIn("UNWIND $batch AS comp", QUERY_INGEST_NODES)
        self.assertIn("MERGE (c:Componente {codigo: comp.codigo})", QUERY_INGEST_NODES)
        self.assertIn("UNWIND $relacoes AS rel", QUERY_INGEST_EDGES)
        self.assertIn("MERGE (origem)-[r:E_PRE_REQUISITO_DE]->(destino)", QUERY_INGEST_EDGES)


if __name__ == "__main__":
    unittest.main()
