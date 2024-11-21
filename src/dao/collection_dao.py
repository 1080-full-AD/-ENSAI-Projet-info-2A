import logging
from src.utils.singleton import Singleton
from src.utils.log_decorator import log
from typing import Optional
from src.business_objet.collection_virtuelle import CollectionVirtuelle
from src.business_objet.manga import Manga
from src.business_objet.utilisateur import Utilisateur

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
                        f"INSERT INTO projet.collection (Titre_collec,"
                        f"id_utilisateur,description) "
                        f"VALUES (%(titre)s, %(id_utilisateur)s ,%(description)s) RETURNING Titre_collec;",
                        {
                            "titre": collection.titre, 
                            "id_utilisateur": collection.id_utilisateur,
                            "description": collection.description
                            
                            }
                            )
                           
                    res = cursor.fetchone()
                
        except Exception as e:
            logging.error("Error creating collection: %s", e)

        if res :
            collection.titre = res["titre_collec"]
            created = True

        return created


    @log
    def ajouter_manga(self, collection: CollectionVirtuelle, manga: Manga)-> bool :

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

                        f" INSERT INTO projet.collection_manga(id_utilisateur,id_manga,"
                        f" titre_collec)  "
                        f" VALUES(%(id_utilisateur)s,%(id_manga)s,%(titre_collec)s)",
                        
                        
                    {

                        "id_utilisateur": collection.id_utilisateur,
                        "id_manga": manga.id_manga,
                        "titre_collec": collection.titre,
                        

                    }
                    )
                res = cursor.rowcount
        except Exception as e:
            logging.error("Error brind collection: %s", e)


        return res == 1      

    @log
    def supprimer_manga(self, collection, manga: Manga) -> bool:

        """supprimer un manga d'une collection virtuelle
        Parameters
        ----------
        manga:manga à supprimer à la collection
        collection:collection de la quelle on doit supprimer le manga 
        Returns
        -------
        bool
        true si le manga a bien été supprimer
        """
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:

                    cursor.execute(

                        f" DELETE FROM projet.collection_manga"
                        f" WHERE id_manga=%(id_manga)s and id_utilisateur=%(id_utilisateur)s  "
                        f" and titre_collec=%(titre)s",
                        
                        
                    {

                        "id_utilisateur": collection.id_utilisateur,
                        "id_manga": manga.id_manga,
                        "titre": collection.titre,
                        
                    }
                    )
                res = cursor.rowcount
        except Exception as e:
            logging.error("Error delete manga: %s", e)


        return res == 1



    @log
    def supprimer_collection(self, collection: CollectionVirtuelle) -> bool:
        
        """Suppression  d'une collection virtuelle existante dans la base de données

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
                        f"DELETE FROM projet.collection_manga   "
                        f"WHERE titre_Collec = %(titre)s AND id_utilisateur = %(id_utilisateur)s;"
                        f" DELETE FROM projet.collection  " 
                        f" WHERE titre_Collec = %(titre)s AND id_utilisateur = %(id_utilisateur)s;",
                        
                            {
                            "titre": collection.titre, 
                            "id_utilisateur": collection.id_utilisateur
                            }
                            )
                      
                    res = cursor.rowcount
        except Exception as e:
            logging.error("Error supprimer collection: %s", e)
            raise

        return res > 0
    

    @log
    def modifier(self, collection:CollectionVirtuelle) -> bool:
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
                        f"   titre_collec = %(titre)s  ,    "
                        f"   id_utilisateur = %(id_utilisateur)s , "
                        f"  description = %(description)s        "
                        f" where titre_collec=%(titre)s AND id_utilisateur = %(id_utilisateur)s", 
                           
                        {
                            "titre": collection.titre,
                            "description": collection.description,
                            "id_utilisateur": collection.id_utilisateur,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.error("Error modifier manga: %s", e)
        return res == 1

    
    def liste_manga(self, collection: CollectionVirtuelle) -> list:
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
                        f"select *     "
                        f"   from projet.collection_manga cm     "
                        f" JOIN projet.manga m USING(id_manga)"
                        f"WHERE cm.id_utilisateur=%(id_utilisateur)s"
                        f"AND cm.titre_collec=%(titre)s", 
                           {
                            "id_utilisateur": collection.id_utilisateur,
                            "titre":collection.titre  
                            }                                
                        )
                    res = cursor.fetchall()
        except Exception as e:
            logging.error("Error lister manga: %s", e)

        liste_manga = []
        if res:
            for row in res:
                manga = Manga(
                    id_manga=row["id_manga"],
                    auteurs=row["auteurs"],
                    titre_manga=row["titre_manga"],
                    synopsis=row["synopsis"]
                     ) 

                liste_manga.append(manga)
        
        return liste_manga 
<<<<<<< HEAD:src/dao/Collection_dao.py

    @log
    def titre_existant(self, collection :CollectionVirtuelle):
        
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
                        f"  select titre_collec    "
                        f"  from projet.collection     "
                        f" WHERE id_utilisateur=%(id_utilisateur)s",
                         
                           {
                            "id_utilisateur": collection.id_utilisateur
                            }                                
                        )
                    res = cursor.fetchall()
        except Exception as e:
            logging.error("Error lister manga: %s", e)

        liste_titre_collec = []
        if res:
            for row in res:
                liste_titre_collec.append(row["titre_collec"])
        
        return collection.titre in liste_titre_collec

    
=======
>>>>>>> db9b9fe54baf12fdc3774b5cf3ee682f367fa65f:src/dao/collection_dao.py
