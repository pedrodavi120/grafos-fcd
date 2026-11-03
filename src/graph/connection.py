# gerenciador de conexao com a base neo4j
import logging
from typing import Optional
from neo4j import GraphDatabase, Driver
from neo4j.exceptions import ServiceUnavailable, AuthError

from src.config import get_neo4j_credentials

logger = logging.getLogger(__name__)


class Neo4jManager:
    # classe para gerenciar o driver e conexoes com o neo4j
    def __init__(self, uri: Optional[str] = None, auth: Optional[tuple] = None, database: Optional[str] = None):
        default_uri, default_auth, default_db = get_neo4j_credentials()
        self.uri = uri or default_uri
        self.auth = auth or default_auth
        self.database = database or default_db
        self._driver: Optional[Driver] = None

    def get_driver(self) -> Driver:
        # cria o driver se ainda nao tiver criado
        if self._driver is None:
            try:
                self._driver = GraphDatabase.driver(self.uri, auth=self.auth)
            except Exception as e:
                logger.error(f"erro ao iniciar driver: {e}")
                raise
        return self._driver

    def check_connection(self) -> bool:
        # testa se o banco ta online e respondendo
        try:
            driver = self.get_driver()
            driver.verify_connectivity()
            return True
        except ServiceUnavailable as e:
            logger.warning(f"neo4j fora do ar em {self.uri}: {e}")
            return False
        except AuthError as e:
            logger.error(f"erro de usuario ou senha no neo4j: {e}")
            return False
        except Exception as e:
            logger.error(f"falha de conexao: {e}")
            return False

    def close(self):
        # fecha o pool de conexao
        if self._driver is not None:
            self._driver.close()
            self._driver = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
