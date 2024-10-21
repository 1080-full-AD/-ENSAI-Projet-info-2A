import os
import dotenv
import psycopg2
from src.utils.singleton import Singleton
from psycopg2.extras import RealDictCursor


class DBConnection(metaclass=Singleton):
    """
    Classe de connexion à la base de données
    Elle permet de n'ouvrir qu'une seule et unique connexion
    """

    def __init__(self):
        """Ouverture de la connexion"""
        dotenv.load_dotenv()

        self.__connection = psycopg2.connect(
            host=os.environ["sgbd-eleves.domensai.ecole"],
            port=os.environ["5432"],
            database=os.environ["POSTGRES_DATABASE"],
            user=os.environ["id2503"],
            password=os.environ["id2503"],
            options=f"-c search_path={os.environ['projet']}",
            cursor_factory=RealDictCursor,
        )

    @property
    def connection(self):
        return self.__connection
