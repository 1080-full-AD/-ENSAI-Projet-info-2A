import logging

from src.utils.singleton import Singleton
from src.utils.log_decorator import log

from src.dao.db_connection import DBConnection

from src.business_objet.manga import Manga


class MangaDao(metaclass=Singleton):
    def trouver_par_titre(self, titre_manga: str) -> Manga:
        """Trouver un manga par le nom exact du tome recherché

        Parameters
        ----------
        titre_manga : le titre du manga recherché : str

        Returns
        -------
        res_manga : les informations à propos du manga trouvé ou None s'il
        n'est pas trouvé
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "FROM projet.manga "
                    f"WHERE titre_manga = '{titre_manga}'"
                )
                res_manga = cursor.fetchone()
            if res_manga:
                res_manga = Manga(
                    titre_manga=res_manga["titre_manga"],
                    id_manga=res_manga["id_manga"],
                    auteurs=res_manga["auteurs"],
                    synopsis=res_manga["synopsis"],
                    nb_volumes=res_manga["nb_volumes"],
                    nb_chapitres=res_manga["nb_chapitres"],
                )
                return res_manga

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

        res = []

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet.manga(id_manga, titre_manga, auteurs, synopsis, nb_volumes, nb_chapitres)"
                        "VALUES                                              "
                        f"('{manga.id_manga}', '{manga.titre_manga}', '{manga.auteurs}', '{manga.synopsis}',"
                        f"'{manga.nb_volumes}', '{manga.nb_chapitres}')"
                        "  RETURNING id_manga;                               ",
                        {
                            "id_manga": manga.id_manga,
                            "titre_manga": manga.titre_manga,
                            "auteurs": manga.auteurs,
                            "synopsis": manga.synopsis,
                            "nb_volumes": manga.nb_volumes,
                            "nb_chapitres": manga.nb_chapitres,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            manga.id_manga = (res["id_manga"],)
            manga.titre_manga = (res["titre_manga"],)
            manga.auteurs = (res["auteurs"],)
            manga.synospsis = (res["synopsis"],)
            manga.nb_volumes = (res["nb_volumes"],)
            manga.nb_chapitres = res["nb_chapitres"]
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
            False sinon
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer un manga de la base de données
                    cursor.execute(
                        f"DELETE FROM projet.manga                  "
                        f" WHERE id_manga= (%(id_manga)s)     ",
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

        res = []

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        f"UPDATE projet.manga                                "
                        f"   SET id_manga      = (%(id_manga)s) ,        "
                        f"       titre_manga         = (%(titre_manga)s) ,           "
                        f"        auteurs       = (%(auteurs)s),           "
                        f"       synopsis      = (%(synopsis)s) ,        "
                        f"       nb_volumes     = (%(nb_volumes)s),"
                        f"       nb_chapitres    = (%(nb_chapitres))"
                        f" WHERE id_manga = (%(id_manga)s) ;             ",
                        {
                            "id_manga": manga.id_manga,
                            "titre_manga": manga.titre_manga,
                            "auteurs": manga.auteurs,
                            "synopsis": manga.synopsis,
                            "nb_volumes": manga.nb_volumes,
                            "nb_chapitres": manga.nb_chapitres,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)

        modif = False
        if res:
            manga.id_manga = (res["id_manga"],)
            manga.titre_manga = (res["titre_manga"],)
            manga.auteurs = (res["auteurs"],)
            manga.synospsis = (res["synopsis"],)
            manga.nb_volumes = (res["nb_volumes"],)
            manga.nb_chapitres = res["nb_chapitres"]
            modif = True

        return modif
        return res == 1

    def trouver_par_id(self, id_manga: str):
        """Trouver un manga par son identifiant s'il est connu (id)

        Parameters
        ----------
        id_manga : identifiant du manga

        Returns
        -------
        res_id_manga : list
            si la modification est un succès
            None sinon
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    f"SELECT titre_manga,"
                    "       id_manga,"
                    "       auteurs,"
                    "       synopsis, "
                    "       nb_volumes,"
                    "       nb_chapitres "
                    "FROM projet.manga "
                    f" WHERE id_manga = %(id_manga)s",
                    {"id_manga": id_manga},
                )
                res_id_manga = cursor.fetchone()
                if res_id_manga:
                    res_id_manga = Manga(
                        titre_manga=res_id_manga["titre_manga"],
                        id_manga=res_id_manga["id_manga"],
                        auteurs=res_id_manga["auteurs"],
                        synopsis=res_id_manga["synopsis"],
                        nb_volumes=res_id_manga["nb_volumes"],
                        nb_chapitres=res_id_manga["nb_chapitres"],
                    )
                    return res_id_manga
                else:
                    return None

    def trouver_par_auteur(self, auteurs) -> Manga:
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
                    "SELECT titre_manga,"
                    "       id_manga,"
                    "       auteurs,"
                    "       synopsis,"
                    "       nb_volumes,"
                    "       nb_chapitres"
                    "       FROM projet.manga "
                    f" WHERE auteurs = '{auteurs}'"
                )
                res_auteur = cursor.fetchall()
                liste_manga_auteur = []
                if res_auteur:
                    for raw_auteur in res_auteur:
                        res_par_auteur = Manga(
                            titre_manga=raw_auteur["titre_manga"],
                            id_manga=raw_auteur["id_manga"],
                            auteurs=raw_auteur["auteurs"],
                            synopsis=raw_auteur["synopsis"],
                            nb_volumes=raw_auteur["nb_volumes"],
                            nb_chapitres=raw_auteur["nb_chapitres"],
                        )
                        liste_manga_auteur.append(res_par_auteur)
                    return liste_manga_auteur
                else:
                    return None

    def trouver_serie_par_titre(self, titre_manga) -> Manga:
        """Trouver la série de manga : par exemple en recherchant "One Piece",
        cela va afficher la liste de tous les tomes de cette sage

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
                    "SELECT id_manga,"
                    "       auteurs,"
                    "       synopsis,"
                    "       titre_manga,"
                    "       nb_volumes,"
                    "       nb_chapitres"
                    " FROM projet.manga "
                    f"WHERE titre_manga = '{titre_manga}'"
                )
                res_serie = cursor.fetchall()
                liste_serie = []
                if res_serie:
                    for raw_serie in res_serie:
                        serie_manga = Manga(
                            titre_manga=raw_serie["titre_manga"],
                            id_manga=raw_serie["id_manga"],
                            auteurs=raw_serie["auteurs"],
                            synopsis=raw_serie["synopsis"],
                            nb_volumes=raw_serie["nb_volumes"],
                            nb_chapitres=raw_serie["nb_chapitres"],
                        )
                        liste_serie.append(serie_manga)
                    return liste_serie
                else:
                    return None
