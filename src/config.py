"""
Módulo de Configuração Central do Projeto.
Carrega parâmetros de ambiente e caminhos de diretórios do padrão Cookiecutter.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env caso exista
load_dotenv()

# Caminhos base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
REPORTS_DIR = BASE_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
REFERENCES_DIR = BASE_DIR / "references"

# Parâmetros de Conexão com o Neo4j
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "senha_teste")
NEO4J_DATABASE = os.getenv("NEO4J_DATABASE", "neo4j")


def get_neo4j_credentials():
    """Retorna a tupla (URI, (USER, PASSWORD), DATABASE) para inicialização do driver."""
    return NEO4J_URI, (NEO4J_USER, NEO4J_PASSWORD), NEO4J_DATABASE

