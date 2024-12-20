import logging
from src.utils.log_decorator import log
from src.utils.singleton import Singleton
from src.business_objet.manga import Manga
from src.business_objet.collection_virtuelle import CollectionVirtuelle
from src.dao.db_connection import DBConnection


class CollectionDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux utilisateurs
    de la base de données"""

    def creer(self, collection: CollectionVirtuelle) -> bool:
        """Creation d'une collection dans la base de données

        Parameters
        ----------
        coLLection : collection
        Returns
        -------
        created : bool
            True si la création est un succès
            False sinon
        """
        created = False

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet.collection (Titre_collec,"
                        " id_utilisateur,description) "
                        " VALUES (%(titre)s, %(id_utilisateur)s "
                        " ,%(description)s)"
                        " RETURNING Titre_collec;",
                        {
                            "titre": collection.titre,
                            "id_utilisateur": collection.id_utilisateur,
                            "description": collection.description,
                        },
                    )

                    res = cursor.fetchone()

        except Exception as e:
            logging.error("Error creer collection: %s", e)

        if res:
            collection.titre = res["titre_collec"]
            created = True

        return created

    @log
    def ajouter_manga(self,
                      collection: CollectionVirtuelle, manga: Manga) -> bool:
        """ajouter un manga  a une collection physique

        Parameters
        ----------
        manga:manga a ajouter à la collection
        collection:collection à la quelle on doit ajouter le manga
        Returns
        -------
        bool
        true si  le manga a été ajouter evec succès

        """
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        " INSERT INTO projet.collection_manga(id_utilisateur,"
                        " id_manga, titre_collec)  "
                        " VALUES(%(id_utilisateur)s,%(id_manga)s,"
                        " %(titre_collec)s)",
                        {
                            "id_utilisateur": collection.id_utilisateur,
                            "id_manga": manga.id_manga,
                            "titre_collec": collection.titre,
                        },
                    )
                res = cursor.rowcount
        except Exception as e:
            logging.error("Error ajouter_manga: %s", e)

        return res == 1

    @log
    def supprimer_manga(self,
                        collection: CollectionVirtuelle, manga: Manga) -> bool:
        """supprimer un manga d'une collection virtuelle
        Parameters
        ----------
        manga:manga à supprimer de la collection
        collection:collection de la quelle on doit supprimer le manga
        Returns
        -------
        bool
        True si le manga a bien été supprimer
        False sinon
        """
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        " DELETE FROM projet.collection_manga"
                        " WHERE id_manga=%(id_manga)s "
                        " AND id_utilisateur=%(id_utilisateur)s  "
                        " AND titre_collec=%(titre)s",
                        {
                            "id_utilisateur": collection.id_utilisateur,
                            "id_manga": manga.id_manga,
                            "titre": collection.titre,
                        },
                    )
                res = cursor.rowcount
        except Exception as e:
            logging.error("Error supprimer_manga: %s", e)

        return res == 1

    @log
    def supprimer_collection(self, collection: CollectionVirtuelle) -> bool:
        """Suppression  d'une collection virtuelle existante dans
         la base de données

        Parameters
        ----------
        coLLection : collection virtuelle à supprimer
        Returns
        -------
        bool
        true si la collection a bien été supprimer
        """
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM projet.collection_manga   "
                        " WHERE titre_Collec = %(titre)s"
                        " AND id_utilisateur = %(id_utilisateur)s;"
                        " DELETE FROM projet.collection  "
                        " WHERE titre_Collec = %(titre)s "
                        " AND id_utilisateur = %(id_utilisateur)s;",
                        {
                            "titre": collection.titre,
                            "id_utilisateur": collection.id_utilisateur,
                        },
                    )

                    res = cursor.rowcount
        except Exception as e:
            logging.error("Error supprimer_collection: %s", e)
            raise

        return res > 0

    @log
    def modifier(self, collection: CollectionVirtuelle) -> bool:
        """Modification d'une collection dans la base de données

        Parameters
        ----------
        collection : collection

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
                        "UPDATE projet.collection  SET   "
                        "  titre_collec = %(titre)s  ,    "
                        "  id_utilisateur = %(id_utilisateur)s , "
                        "  description = %(description)s        "
                        "  WHERE titre_collec=%(titre)s "
                        "  AND id_utilisateur = %(id_utilisateur)s",
                        {
                            "titre": collection.titre,
                            "description": collection.description,
                            "id_utilisateur": collection.id_utilisateur,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.error("Error modifier : %s", e)
        return res == 1

    @log
    def modifier_titre(self,
                       collection: CollectionVirtuelle,
                       new_titre: str) -> bool:
        """Modification du titre d'une collection dans la base de données

        Parameters
        ----------
        collection : collection
        new_titre : nouveau titre de la collection
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
                        "   UPDATE projet.collection  SET   "
                        "  titre_collec = %(new_titre)s      "
                        "  WHERE titre_collec=%(titre)s "
                        "  AND id_utilisateur = %(id_utilisateur)s ;",
                        {
                            "new_titre": new_titre,
                            "titre": collection.titre,
                            "id_utilisateur": collection.id_utilisateur,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.error("Error modifier_titre : %s", e)
        return res >= 1

    @log
    def liste_manga(self, id_utilisateur: int, titre_collec: str) -> list:
        """liste tous les mangas d'une collection virtuelle
        Parameters
        ----------
        collection : collection virtuelle

        Returns
        -------
        liste_manga : list[manga]
            retourne la liste de tous les mangas de la collections

        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "select *     "
                        " FROM projet.collection_manga cm     "
                        " JOIN projet.manga m USING(id_manga)"
                        " WHERE cm.id_utilisateur = %(id_utilisateur)s"
                        " AND cm.titre_collec = %(titre)s",
                        {"id_utilisateur": id_utilisateur,
                         "titre": titre_collec},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.error("Error liste_manga: %s", e)

        liste_manga = []
        if res:
            for row in res:
                manga = Manga(
                    id_manga=row["id_manga"],
                    auteurs=row["auteurs"],
                    titre_manga=row["titre_manga"],
                    synopsis=row["synopsis"],
                    nb_volumes=row["nb_volumes"],
                    nb_chapitres=row["nb_chapitres"],
                )

                liste_manga.append(manga)

        return liste_manga

    @log
    def titre_existant(self, titre: str, id_utilisateur: int) -> bool:
        """indique si le titre de la collection est presente dans la
            base de données pour le même utilisateur

        Parameters
        ----------
        collection : collection pour la quelle on fait la vérification

        Returns
        -------
        bool
        true si le titre est déja enregistré dans la base de donnée
        pour le même utilisateur
        False sinon

        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "  SELECT titre_collec    "
                        "  FROM projet.collection     "
                        "  WHERE id_utilisateur=%(id_utilisateur)s",
                        {"id_utilisateur": id_utilisateur},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.error("Error titre_existant: %s", e)

        liste_titre_collec = []
        if res:
            for row in res:
                liste_titre_collec.append(row["titre_collec"])

        return titre in liste_titre_collec

    @log
    def liste_collection(self, id_utilisateur: int) -> list:
        """retourne la liste des collections virtuelles d'un utilisateur
        qui sont enregistré dans la base de données

        Parameters
        ----------
        id-utilisateur : identifiant de l'utilisateur

        Returns
        -------
        list[CollectionVirtuelle]
        la liste des collections virtuelles de l'utilisateur

        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "  SELECT *    "
                        "  FROM projet.collection     "
                        "  WHERE id_utilisateur=%(id_utilisateur)s",
                        {"id_utilisateur": id_utilisateur},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.error("Error liste_collection: %s", e)

        liste_collection = []
        if res:
            for row in res:
                liste_mangas = self.liste_manga(
                    id_utilisateur=row["id_utilisateur"],
                    titre_collec=row["titre_collec"],
                )
                collection = CollectionVirtuelle(
                    titre=row["titre_collec"],
                    id_utilisateur=row["id_utilisateur"],
                    liste_manga=liste_mangas,
                    description=row["description"],
                )
                liste_collection.append(collection)

        return liste_collection

    @log
    def recherhcer_collection(
        self, id_utilisateur: int, titre_collec: str
    ) -> CollectionVirtuelle:
        """Retourne la collecttion virtuelle qui correspond à
        l'identifiant de l'utilisateur et au titre renseigné

         Parameters
         ----------
         id-utilisateur : identifiant de l'utilisateur
         titre_collec :titre de la collection
         Returns
         -------
        CollectionVirtuelle
        la collection virtuelle trouvé ou
        None si aucune collection n'est trouvée

        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "  SELECT *    "
                        "  FROM projet.collection     "
                        "  WHERE id_utilisateur=%(id_utilisateur)s"
                        "  AND titre_collec=%(titre_collec)s",
                        {
                            "id_utilisateur": id_utilisateur,
                            "titre_collec": titre_collec,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.error("Error rechercher_collection : %s", e)

        if res:
            liste_mangas = self.liste_manga(
                id_utilisateur=res["id_utilisateur"],
                titre_collec=res["titre_collec"]
            )
            collection = CollectionVirtuelle(
                titre=res["titre_collec"],
                id_utilisateur=res["id_utilisateur"],
                liste_manga=liste_mangas,
                description=res["description"],
            )

            return collection

        else:
            return res
