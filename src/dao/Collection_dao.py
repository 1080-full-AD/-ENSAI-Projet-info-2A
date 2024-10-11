import logging
from typing import List, Optional
from utils.singleton import Singleton
from src.business_objet.Collection.Abstract_Collection import AbstractCollection 
from src.business_objetuisness_objet.manga import manga
from src.dao.db_connection import DBConnection


class CollectionDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux utilisateurs
       de la base de données"""

    def Creer_Collection(self, Collection: AbstractCollection) -> bool:

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
                    "VALUES                                                     "
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
            attack.titre= res["titre"]
            created = True

        return created

    def trouver_par_titre(titre: str) -> Optional[AbsractCollection]:

        """Recherche d'une collection dans la base de données à partir de son titre

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
                collection = COllectionVirtuelle(
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


def supprimer_collection(self,manga) -> None:

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
                            {"titre":manga.titre}
            )
        

