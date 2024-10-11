import logging

from src.utils.singleton import Singleton
from src.utils.log_decorator import log

from src.dao.db_connection import DBConnection

from src.business_objet.utilisateur import Utilisateur


class UtilisateurDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux utilisateurs
       de la base de données"""

    @log
    def creer(self, utilisateur) -> bool:
        """Creation d'un utilisateur dans la base de données

        Parameters
        ----------
        utilisateur : Utilisateur

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
                        "INSERT INTO utilisateur(pseudo, mdp,"
                        "age, collections) VALUES                            "
                        "(%(pseudo)s, %(mdp)s, %(age)s,                      "
                        "%(collections)s)                          "
                        "  RETURNING id_utilisateur;                         ",
                        {
                            "pseudo": utilisateur.pseudo,
                            "mdp": utilisateur.mdp,
                            "age": utilisateur.age,
                            "collections": utilisateur.collections
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            utilisateur.id_utilisateur = res["id_utilisateur"]
            created = True

        return created

    @log
    def trouver_par_pseudo(self, pseudo:str) -> Utilisateur:
        """trouver un utilisateur grace à son pseudo

        Parameters
        ----------
        pseudo : str
            pseudo de l'utilisateur que l'on souhaite trouver

        Returns
        -------
        utilisateur : Utilisateur
            renvoie l'utilisateur que l'on cherche
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "FROM utilisateur                      "
                        " WHERE pseudo = %(pseudo)s;  ",
                        {"pseudo": pseudo},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        utilisateur = None
        if res:
            utilisateur = Utilisateur(
                pseudo=res["pseudo"],
                age=res["age"],
                collections=res["collections"],
                id_joueur=res["id_utilisateur"],
            )

        return utilisateur

    @log
    def lister_tous(self) -> list[Utilisateur]:
        """lister tous les utilisateur

        Parameters
        ----------
        None

        Returns
        -------
        liste_utilisateur : list[Utilisateur]
            renvoie la liste de tous les utilisateur dans la base de données
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                              "
                        "  FROM utilisateur;                        "
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        liste_utilisateurs = []

        if res:
            for row in res:
                utilisateur = Utilisateur(
                    id_utilisateur=row["id_utilisateur"],
                    pseudo=row["pseudo"],
                    mdp=row["mdp"],
                    age=row["age"],
                    collections=row["collections"]
                )

                liste_utilisateurs.append(utilisateur)

        return liste_utilisateurs

    @log
    def modifier(self, utilisateur) -> bool:
        """Modification d'un utilisateur dans la base de données

        Parameters
        ----------
        utilisateur : Utilisateur

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
                        "UPDATE utilisateur                                 "
                        "   SET pseudo      = %(pseudo)s,                   "
                        "       mdp         = %(mdp)s,                      "
                        "       age         = %(age)s,                      "
                        "       collections = %(collections)s               "
                        " WHERE id_joueur = %(id_joueur)s;                  ",
                        {
                            "pseudo": utilisateur.pseudo,
                            "mdp": utilisateur.mdp,
                            "age": utilisateur.age,
                            "collections": utilisateur.collections,
                            "id_utilisateur": utilisateur.id_utilisateur,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)

        return res == 1

    @log
    def supprimer(self, utilisateur) -> bool:
        """Suppression d'un utilisateur dans la base de données

        Parameters
        ----------
        utilisateur : Utilisateur
            utilisateur à supprimer de la base de données

        Returns
        -------
            True si le utilisateur a bien été supprimé
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer le compte d'un utilisateur
                    cursor.execute(
                        "DELETE FROM utilisateur                  "
                        " WHERE id_utilisateur=%(id_utilisateur)s      ",
                        {"id_utilisateur": utilisateur.id_utilisateur},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0
