from dao.db_connection import DBConnection
from manga.py import Manga


class MangaDAO(metaclass=Singleton):

    def trouver_par_titre(self, titre: str) -> Manga:
        """Trouver un manga par son nom"""
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT titre,"
                    "       id_manga,"
                    "       auteur,"
                    "       synopsis,"
                    "FROM manga"
                    "WHERE nom = %(titre)s",
                    )
                res_manga = cursor.fetchone()
            if res_manga:
                res_manga = Manga(
                    titre=res_manga["titre"],
                    id_manga=res_manga["id_manga"],
                    auteur=res_manga["auteur"],
                    synopsis=res_manga["synopsis"]
                    )
                return res_manga
            else:
                return None

    def trouver_par_id(self, id: str) -> Manga:
        """Trouver un manga par son identifiant s'il est connu (id)"""
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT titre,"
                    "       id_manga,"
                    "       auteur,"
                    "       synopsis,"
                    "FROM manga"
                    "WHERE id = %(id_manga)s",
                    {id : "id"}
                    )
                res_id_manga = cursor.fetchone()
            if res_id_manga:
                res_id_manga = Manga(
                    titre=res_id_manga["titre"],
                    id_manga=res_id_manga["id_manga"],
                    auteur=res_id_manga["auteur"],
                    synopsis=res_id_manga["synopsis"]
                    )
                return res_id_manga
            else:
                return None


