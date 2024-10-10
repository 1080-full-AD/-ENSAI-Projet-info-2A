import logging
from typing import List, Optional
from utils.singleton import Singleton
from Buisness_objet.Collection.Abstract_Collection import AbstractCollection 
from Buisness_objet.manga import manga 


class CollectionDao(metaclass=Singleton):
    def Creer_Collection(self, Collection: AbstractCollection) -> bool:
        """
        Ajouter une collection à la base de données 
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

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:

                cursor.execute(
                    "Select * from collection where titre=%(titre)s", {"titre": titre}
                )
                res = cursor.fetchone()

    #si cles elements de liste_manga sont des dictionnaires alors :........ 