import logging

from src.utils.singleton import Singleton
from src.utils.log_decorator import log

from src.dao.db_connection import DBConnection

from src.Business_objet.manga import Manga


class MangaDAO(metaclass=Singleton):

    def trouver_par_titre(self, titre: str) -> Manga:
        """Trouver un manga par son nom

        Parameters
        ----------
        titre : le titre du manga recherché : str

        Returns
        -------
        res_manga : les informationqs à propos du manga trouvé ou None s'il
        n'est pas trouvé
        """
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

    @log
    def creer_manga(self, manga) -> bool:
        """Creation d'un manga dans la base de données

        Parameters
        ----------
        manga : Manga

        Returns
        -------
        created : bool
            True si la création est un succès
            False sinon
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO manga(id_manga, titre, auteur, synopsis, )VALUES"
                        "(%(id_manga)s, %(titre)s, %(auteur)s, %(synopsis)s) "
                        "  RETURNING id_manga;                               ",
                        {
                            "id_manga": manga.id_manga,
                            "titre": manga.titre,
                            "auteur": manga.auteur,
                            "synopsis": manga.synopsis
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            manga.id_manga = res["id_manga"]
            created = True

        return

    @log
    def supprimer_manga(self, manga) -> bool:
        """Suppression d'un manga dans la base de données

        Parameters
        ----------
        manga : Manga
            manga à supprimer de la base de données

        Returns
        -------
            True si le manga a bien été supprimé
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer un manga de la base de données
                    cursor.execute(
                        "DELETE FROM manga                  "
                        " WHERE id_manga=%(id_manga)s      ",
                        {"id_manga": manga.id_manga},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0

    @log
    def modifier(self, manga) -> bool:
        """Modification d'un manga dans la base de données

        Parameters
        ----------
        manga : Manga

        Returns
        -------
        created : bool
            True si la modification est un succès
            False sinon
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE manga                                "
                        "   SET id_manga      = %(id_manga)s,        "
                        "       titre         = %(titre)s,           "
                        "        auteur       = %(auteur)s           "
                        "       synopsis      = %(synopsis)s,        "
                        " WHERE id_manga = %(id_manga)s;             ",
                        {
                            "id_manga": manga.id_manga,
                            "titre": manga.titre,
                            "auteur": manga.auteur,
                            "synopsis": manga.synopsis
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)

        return res == 1


# def trouver_par_id(self, id: str) -> Manga:
#        """Trouver un manga par son identifiant s'il est connu (id)"""
#       with DBConnection().connection as connection:
#          with connection.cursor() as cursor:
#               cursor.execute(
#                   "SELECT titre,"
#                   "       id_manga,"
#                   "       auteur,"
#                   "       synopsis,"
#                   "FROM manga"
#                   "WHERE id = %(id_manga)s",
#                   {'id' : id}
#                   )
#               res_id_manga = cursor.fetchone()
#           if res_id_manga:
#               res_id_manga = Manga(
#                   titre=res_id_manga["titre"],
#                   id_manga=res_id_manga["id_manga"],
#                   auteur=res_id_manga["auteur"],
#                  synopsis=res_id_manga["synopsis"]
#                   )
#              return res_id_manga
#            else:
#               return None
