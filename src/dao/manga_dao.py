import logging

from src.utils.singleton import Singleton
from src.utils.singleton import Singleton
from src.utils.log_decorator import log

from src.dao.db_connection import DBConnection

from src.business_objet.manga import Manga


class MangaDao(metaclass=Singleton):

    def trouver_par_titre(self, titre: str) -> Manga:
        """Trouver un manga par le nom exact du tome recherché
        Trouver un manga par le nom exact du tome recherché

        Parameters
        ----------
        titre : le titre du manga recherché : str

        Returns
        -------
        res_manga : les informations à propos du manga trouvé ou None s'il
        n'est pas trouvé
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
<<<<<<< HEAD
                    "FROM manga "
                    f"WHERE nom = '{titre}'"
=======
                    "FROM projet.manga "
                    f"WHERE titre_manga = '{titre}'"
>>>>>>> 79ad0fab76fb97e24949783ae76dd20d01d2d307
                    )
                res_manga = cursor.fetchone()
            if res_manga:
                res_manga = Manga(
                    titre=res_manga["titre_manga"],
                    id_manga=res_manga["id_manga"],
                    auteur=res_manga["auteurs"],
                    synopsis=res_manga["synopsis"]
                    )
                print("OK")
                print("OK")
                return res_manga
            else:
                print("fail")
                print("fail")

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
                        "INSERT INTO manga(id_manga, titre, auteur, synopsis)"
                        "VALUES                                              "
                        f"('{id_manga}', '{titre}', '{auteur}', '{synopsis}') "
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

        return created

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
                        f" WHERE id_manga='{id_manga}'      ",
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
                        f"   SET id_manga      = '{id_manga}',        "
                        f"       titre         = '{titre}',           "
                        f"        auteur       = '{auteur}'           "
                        f"       synopsis      = '{synopsis}',        "
                        f" WHERE id_manga = '{id_manga}';             ",
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
                  f"WHERE id = '{id_manga}'",
                  {'id': id}
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

    def trouver_par_auteur(self, auteur) -> Manga:
        """Trouver un manga grâce au nom de son auteur

        Parameters
        ----------
        manga : Manga

        Returns
        -------
        liste_manga_auteur : list
            affiche la liste de tous les mangas écrits par cet auteur si le
            résultat est trouvé
            sinon cela affiche None
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                  "SELECT titre,"
                  "       id_manga,"
                  "       auteur,"
                  "       synopsis,"
                  "FROM manga"
                  f"WHERE auteur = '{auteur}'"
                   )
                res_auteur = cursor.fetchall()
                liste_manga_auteur = []
                if res_auteur:
                    for raw_auteur in res_auteur:
                        manga_par_auteur = Manga(
                            titre=raw_auteur["titre"],
                            id_manga=raw_auteur["id_manga"],
                            auteur=raw_auteur["auteur"],
                            synopsis=raw_auteur["synopsis"]
                        )
                    liste_manga_auteur.append(manga_par_auteur)
                    return liste_manga_auteur
                else:
                    return None

    def trouver_serie_par_titre(self, manga) -> Manga:
        """Trouver la série de manga : par exemple en recherchant "One Piece", 
        cela va afficher laliste de tous les tomes de cette sage

        Parameters
        ----------
        manga : Manga

        Returns
        -------
        liste_serie: list
            affiche la liste de tous les tomes des mangas se trouvant 
            dans la saga
            sinon cela affiche None
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                  "SELECT titre,"
                  "       id_manga,"
                  "       auteur,"
                  "       synopsis,"
                  "FROM manga"
                  f"WHERE auteur = '{auteur}'"
                   )
                res_serie = cursor.fetchall()
                liste_serie = []
                if res_serie:
                    for raw_serie in res_serie:
                        serie_manga = Manga(
                            titre=raw_serie["titre"],
                            id_manga=raw_serie["id_manga"],
                            auteur=raw_serie["auteur"],
                            synopsis=raw_serie["synopsis"]
                        )
                    liste_serie.append(serie_manga)
                    return liste_serie
                else:
                    return None


print(MangaDao().trouver_par_titre("Monster").titre)