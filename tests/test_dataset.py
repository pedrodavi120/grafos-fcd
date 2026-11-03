"""
Testes automatizados para validação e integridade do dataset curricular.
Garante o Pilar I (Zero Mock em Produção) e integridade referencial estrita.
Compatível com unittest padrão e pytest.
"""

import unittest
from src.config import RAW_DATA_DIR, PROCESSED_DATA_DIR
from src.data.make_dataset import process_disciplinas, process_prerequisitos


class TestDatasetIntegrity(unittest.TestCase):
    """Testes de conformidade e integridade dos dados curriculares."""

    def test_raw_files_exist(self):
        """Garante a presença dos arquivos brutos fundamentais."""
        self.assertTrue((RAW_DATA_DIR / "tads_disciplinas.csv").exists())
        self.assertTrue((RAW_DATA_DIR / "tads_prerequisitos.csv").exists())

    def test_processed_disciplinas_integrity(self):
        """Valida as restrições de negócio e tipos das disciplinas."""
        raw_path = RAW_DATA_DIR / "tads_disciplinas.csv"
        df = process_disciplinas(raw_path)

        # Chave primária única
        self.assertFalse(df["codigo"].duplicated().any())
        # Cargas horárias estritamente positivas
        self.assertTrue((df["ch"] > 0).all())
        # Semestres entre 1 e 6
        self.assertTrue(df["semestre"].between(1, 6).all())
        # Deve conter componentes obrigatorios essenciais com codigos oficiais
        self.assertIn("TAD0102", df["codigo"].values)
        self.assertIn("TAD0103", df["codigo"].values)
        self.assertIn("TAD0204", df["codigo"].values)

    def test_processed_prerequisitos_referential_integrity(self):
        """Valida ausência de arestas órfãs e ausência de autorrelacionamento."""
        raw_disc = RAW_DATA_DIR / "tads_disciplinas.csv"
        raw_pre = RAW_DATA_DIR / "tads_prerequisitos.csv"

        df_disc = process_disciplinas(raw_disc)
        codigos_validos = set(df_disc["codigo"])
        df_pre = process_prerequisitos(raw_pre, codigos_validos)

        self.assertFalse((df_pre["codigo_origem"] == df_pre["codigo_destino"]).any())
        self.assertTrue(set(df_pre["codigo_origem"]).issubset(codigos_validos))
        self.assertTrue(set(df_pre["codigo_destino"]).issubset(codigos_validos))


if __name__ == "__main__":
    unittest.main()
