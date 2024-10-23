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
                        "INSERT INTO projet.utilisateur(pseudo, mot_de_passe,"
                        "age) VALUES                            "
                        f"('{utilisateur.pseudo}', '{utilisateur.mdp}', {utilisateur.age})"
                        "  RETURNING id_utilisateur;                         ",
                        {
                            "pseudo": utilisateur.pseudo,
                            "mdp": utilisateur.mdp,
                            "age": utilisateur.age,
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
    def trouver_par_pseudo(self, pseudo: str) -> Utilisateur:
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
                        f" WHERE pseudo = '{pseudo}';  ",
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
                        "FROM projet.utilisateur                      "
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
                    mdp=row["mot_de_passe"],
                    age=row["age"],
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
                        f"   SET pseudo      = '{pseudo}',                   "
                        f"       mdp         = '{mdp}',                      "
                        f"       age         = '{age}',                      "
                        f"       collections = '{collections}'               "
                        f" WHERE id_joueur = '{id_joueur}';                  ",
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
                        f" WHERE id_utilisateur='{id_utilisateur}'      ",
                        {"id_utilisateur": utilisateur.id_utilisateur},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0
    
    @log
    def se_connecter(self, pseudo, mdp) -> Utilisateur:
        """se connecter grâce à son pseudo et son mot de passe

        Parameters
        ----------
        pseudo : str
            pseudo de l'utilisateur que l'on souhaite trouver
        mdp : str
            mot de passe de l'utilisateur

        Returns
        -------
        utilisateur : Utilisateur
            renvoie l'utilisateur que l'on cherche
        """
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM projet.utilisateur                      "
                        f" WHERE pseudo = '{pseudo}'         "
                        f"   AND mod_de_passe = '{mdp}';              ",
                        {"pseudo": pseudo, "mot_de_passe": mdp},
                    )
                    res = cursor.fetchone()

        except Exception as e:
            logging.info(e)

        utilisateur = None
        print(res)
        if res:
            utilisateur = Utilisateur(
                pseudo=res["pseudo"],
                mdp=res["mdp"],
                age=res["age"],
                id_utilisateur=res["id_utilisateur"]
            )

        return utilisateur


print(UtilisateurDao().se_connecter('drop table', 'Adrien44'))
