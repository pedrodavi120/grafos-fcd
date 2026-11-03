# definicao das restricoes e indices cypher
from typing import Any

# constraint para nao duplicar codigo de disciplina
CONSTRAINT_COMPONENTE_CODIGO = """
CREATE CONSTRAINT unique_componente_codigo IF NOT EXISTS
FOR (c:Componente)
REQUIRE c.codigo IS UNIQUE;
"""

# indice para acelerar busca por semestre
INDEX_COMPONENTE_SEMESTRE = """
CREATE INDEX idx_componente_semestre IF NOT EXISTS
FOR (c:Componente)
ON (c.semestre);
"""

# comando para limpar o grafo caso precise resetar
QUERY_CLEAR_ALL = """
MATCH (n:Componente)
DETACH DELETE n;
"""


def apply_schema(session: Any) -> None:
    # roda as constraints e indices na sessao
    session.run(CONSTRAINT_COMPONENTE_CODIGO)
    session.run(INDEX_COMPONENTE_SEMESTRE)
