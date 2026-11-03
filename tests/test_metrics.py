"""
Testes automatizados para algoritmos de Teoria dos Grafos (NetworkX).
Compatível com unittest padrão e pytest.
"""

import unittest
import networkx as nx
from src.analysis.graph_metrics import (
    load_graph_from_processed,
    calculate_centralities,
    find_critical_paths,
    get_k_hop_successors
)


class TestGraphMetrics(unittest.TestCase):
    """Testes de conformidade analítica em redes complexas."""

    @classmethod
    def setUpClass(cls):
        cls.G = load_graph_from_processed()

    def test_graph_is_valid_dag(self):
        """Valida se o grafo curricular é um Grafo Direcionado Acíclico (sem loops temporais)."""
        self.assertGreater(self.G.number_of_nodes(), 0)
        self.assertGreater(self.G.number_of_edges(), 0)
        self.assertTrue(nx.is_directed_acyclic_graph(self.G), "O grafo curricular não pode conter ciclos!")

    def test_centrality_calculations(self):
        """Valida o cálculo das métricas de centralidade."""
        df = calculate_centralities(self.G)

        self.assertEqual(len(df), self.G.number_of_nodes())
        self.assertIn("betweenness_centrality", df.columns)
        self.assertIn("in_degree", df.columns)
        self.assertIn("out_degree", df.columns)

        # TAD0102 (Algoritmos e Programacao) deve ser um dos maiores provedores de pre-requisitos
        row_tad0102 = df[df["codigo"] == "TAD0102"].iloc[0]
        self.assertGreaterEqual(row_tad0102["out_degree"], 3)

    def test_critical_path_detection(self):
        """Valida o cálculo do caminho crítico de formatura."""
        critical = find_critical_paths(self.G)
        self.assertGreater(len(critical), 0)
        length, path = critical[0]
        self.assertGreaterEqual(length, 4)
        self.assertEqual(path[0], "TAD0102")  # O caminho mais longo parte de Algoritmos

    def test_k_hop_traversal(self):
        """Valida a simulação de travessias de múltiplos saltos."""
        successors = get_k_hop_successors(self.G, "TAD0102", k=3)

        self.assertIn(1, successors)
        self.assertIn(2, successors)
        self.assertIn(3, successors)
        # Algoritmos tem pré-requisitos diretos no salto 1
        self.assertIn("TAD0009", successors[1])
        self.assertIn("TAD0020", successors[1])
        # No salto 2, deve alcançar FCD via Banco de Dados ou Estruturas de Dados
        self.assertIn("TAD0204", successors[2])


if __name__ == "__main__":
    unittest.main()
