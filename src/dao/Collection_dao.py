import logging
from src.utils.singleton import Singleton
from src.utils.log_decorator import log
from typing import Optional


from src.business_objet.collection.abstract_collection import AbstractCollection 
from src.business_objet.collection.collection_physique import CollectionPhysique
from src.business_objet.collection.collection_virtuelle import CollectionVirtuelle
from src.business_objet.manga import Manga

from src.dao.db_connection import DBConnection


class CollectionDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux utilisateurs
       de la base de données"""

    def Creer(self, collection: AbstractCollection) -> bool:

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
        try: 
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO Collection (id_collection, titre, "
                        " id_utilisateur,liste_manga)             "
                        "VALUES                                   "
                        "(%(id_collection)s,%(titre)s, %(id_utilisateur)s"
                        ", %(liste_manga)s )   "
                   
                        "RETURNING titre;",
                        {
                            "id_collection": collection.id_collection,
                            "titre": collection.titre,
                            "id_utilisateur": collection.id_utilisateur,
                            "liste_manga": collection.liste_manga,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        if res:
            collection.titre = res["titre"]
            created = True

        return created

    @log
    def trouver_par_titre(titre: str) -> Optional[AbstractCollection]:

        """Recherche d'une collection dans la base de données à partir de son
         titre

        Parameters
        ----------
        titre:titre de la collection à rechercher
        Returns
        -------
        collection
            liste de dictionnaire des utilisateurs et des collections 
            des utilisateurs qui correspondent au titre recherché
            
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:

                    cursor.execute(
                        "Select c.*,u.pseudo"
                        " from collection c"
                        "join utilisateur using(id_utilisateur)"
                        "where titre=%(titre)s", 
                        {"titre": titre}
                    )
                res = cursor.fetchall()

        except Exception as e:
            logging.info(e)

        liste_collection = []
        if res:
            for row in res:
                if row["type"] == "virtuelle":
                    collection = CollectionVirtuelle(
                                id_collection=row["id_collection"],
                                titre=row["titre"],
                                id_utilisateur=row["id_utilisateur"],
                                liste_manga=row["liste_manga"],
                    
                        )
            
                else:
                    collection = CollectionPhysique(
                                    id_collection=row["id_collection"],
                                    titre=res["titre"],
                                    id_utilisateur=res["id_utilisateur"],
                                    liste_manga=res["liste_manga"],
                        )
                liste_collection.append({"utilisateur": row["pseudo"],
                                        "collection": collection}, )
            return liste_collection
        else:
            return None


@log
def supprimer(self, collection) -> None:
        
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
            
                           "where id_collection=%(id_collection)s",
                           {"id_collection": collection.id_collection}

                           )

    @log
    def modifier(self, collection) -> bool:
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
                        "UPDATE collection      "
                        "   titre = %(titre)s,       "
                        "   id_utilisateur = %(id_utilisateur)s,    "
                        "   list_manga = %(list_manga)s,                      "
                        "where id_collection=%(id_collection)s",
                       
                        {
                            "titre": collection.titre,
                            "list_manga": collection.list_manga,
                            "id_collection": collection.id_collection
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)

        return res == 1

    def liste_manga(self, collection) -> list:
        """liste tous les mangas d'une collection
        Parameters
        ----------
        collection : collection

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
                        "select m.*      "
                        "   from collection c       "
                        "   join manga m using id.manga " 
                        "where c.id_collection=%(id_collection)s",
                        {"titre": collection.titre}                                   
                        )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)

        liste_manga = []
        if res:
            for row in res:
                manga = Manga(
                    id_manga=row["id.manga"],
                    auteur=row["auteur"],
                    titre=row["titre"],
                    synopsis=row["synopsis"]
                     ) 

                liste_manga.append(manga)
        
        return liste_manga 