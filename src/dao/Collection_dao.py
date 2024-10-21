import logging
from typing import List, Optional

from utils.singleton import Singleton
from src.utils.log_decorator import log

from src.business_objet.collection.abstract_Collection import AbstractCollection 
from src.business_objet.collection.collection_physique import CollectionPhysique
from src.business_objet.collection.collection_virtuelle import CollectionVirtuelle


from src.dao.db_connection import DBConnection


class CollectionDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux utilisateurs
       de la base de données"""

    def Creer_Collection(self, collection: AbstractCollection) -> bool:

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

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Collection (titre, id_utilisateur,        "
                    " liste_manga)             "
                    "VALUES                                                "
                    "(%(titre)s, %(id_utilisateur)s, %(liste_manga)s    "
                   
                    "RETURNING titre;",
                    {
                        "titre": collection.titre,
                        "id_utilisateur": collection.id_utilisateur,
                        "liste_manga": collection.liste_manga,
                    },
                )
                res = cursor.fetchone()
        if res:
            collection.titre = res["titre"]
            created = True

        return created

    def trouver_par_titre(titre: str) -> Optional[AbstractCollection]:

        """Recherche d'une collection dans la base de données à partir de son
         titre

        Parameters
        ----------
        titre:titre de la collection à rechercher
        Returns
        -------
        collection
            la collection si elle a été crée 
            
        """

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:

                cursor.execute(
                    "Select * from collection where titre=%(titre)s", {"titre": titre}
                )
                res = cursor.fetchone()

                if res:
                    if res["type"] == "virtuelle":
                        collection = CollectionVirtuelle(
                                    titre=res["titre"],
                                    id_utilisateur=res["id_utilisateur"],
                                    liste_manga=res["liste_manga"],
                    
                        )
            
                    else:
                        collection = CollectionPhysique(
                                    titre=res["titre"],
                                    id_utilisateur=res["id_utilisateur"],
                                    liste_manga=res["liste_manga"],
                        )

                    return collection
                else:
                    return None


def supprimer_collection(self, collection) -> None:

    """Suppression  d'une collection existante dans la base de données

        Parameters
        ----------
        coLLection : collection à supprimer
        Returns
        -------
        None
        """
    with DBConnection().connection as connection:
        with connection.cursor() as cursor:

            cursor.execute("delete from collection"
            
                            "where titre=%(titre)s",
                            {"titre": collection.titre}
                          )
        


    @log
    def modifier_titre(self, collection, new_titre) -> bool:
        """Modification du titre d'une collection dans la base de données

        Parameter
        ----------
        collection : collection à modifier
        new_titre:nouveau titre de la collection
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
                        "UPDATE collection "
                        "   SET titre= %(new_titre)s, " 
                        " WHERE titre = %(titre)s;  ",
                        {
                            "titre": collection.titre,
                            "new_titre": new_titre,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)

        return res == 1



    @log
    def modifier_liste_manga(self, collection, manga) -> bool:
        """Modification du titre d'une collection dans la base de données

        Parameter
        ----------
        collection : collection à modifier
        new_titre:nouveau titre de la collection
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
                        "UPDATE collection "
                        "   SET titre= %(new_titre)s, " 
                        " WHERE titre = %(titre)s;  ",
                        {
                            "titre": collection.titre,
                            "new_titre": new_titre,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)

        return res == 1
