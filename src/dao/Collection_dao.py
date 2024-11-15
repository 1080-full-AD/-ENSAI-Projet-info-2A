import logging
from src.utils.singleton import Singleton
from src.utils.log_decorator import log
from typing import Optional


from src.business_objet.collection.abstract_collection import AbstractCollection
from src.business_objet.collection.collection_physique import CollectionPhysique
from src.business_objet.collection.collection_virtuelle import CollectionVirtuelle
from src.business_objet.manga import Manga
from src.business_objet.manga_physique import MangaPhysique

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
            collection.titre = res["Titre_collec"]
            created = True

        return created

    
        
        


    @log
    def ajouter_manga_virtuelle(self,collection:CollectionVirtuelle, manga:Manga)-> bool :

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
                        f" VALUES(%(id_utilisateur)s,%(id_manga)s,%(titre_collec)s,",
                        
                        
                    {

                        "id_utilisateur": collection.id_utilisateur,
                        "id_manga": manga.id_manga,
                        "titre_collec": collection.titre,
                        

                    }
                    )
                res = cursor.rowcount
        except Exception as e:
            logging.info(e)

        return res == 1




    
                    
      

    @log
    def supprimer_manga_virtuel(self, manga:Manga)->bool:

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

                        f" deLETE FROM projet.collection_manga"
                        f"wHeRe id_manga=%(id_manga) and id_utilisateur=%(id_utilisateur)  "
                        f" and titre_collec=%(titre),",
                        
                        
                    {

                        "id_utilisateur": collection.id_utilisateur,
                        "id_manga": manga.id_manga,
                        "titre": collection.titre,
                        
                    }
                    )
                res = cursor.rowcount
        except Exception as e:
            logging.info(e)

        return res == 1

        
     
    


    @log
    def supprimer_collection_virtuelle(self, collection: CollectionVirtuelle)->bool:
        
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
                        f" DELETE FROM projet.collection" 
                        f" WHERE titre_Collec = %(titre)s AND id_utilisateur = %(id_utilisateur)s;"
                        f"DELETE FROM projet.collection_manga"
                        f"WHERE titre_Collec = %(titre)s AND id_utilisateur = %(id_utilisateur)s;",
                            {
                            "titre": collection.titre, 
                            "id_utilisateur": collection.id_utilisateur
                            }
                            )
                      
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0
    

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
                        "UPDATE projet.collection      "
                        f"   titre_collec = %(titre)s       "
                        f"   id_utilisateur = %(id_utilisateur)   "
                        f"  description = %(descritpion)s                      "
                        f"where titre=%(titre)s and id_utilisateur=%(id_utilisateur)s", 
                           
                        {
                            "titre": collection.titre_collec,
                            "description": collection.description,
                            "id_utilisateur": collection.id_utilisateur,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)

        return res ==1

    def liste_manga_physique(self, collection) -> list:
        """liste tous les mangas d'une collection physique
        Parameters
        ----------
        collection : collection physique

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
                        f"   from projet.mangatheque mt     "
                        f" JOIN projet.manga m USING(id_manga)"
                        f"WHERE mt.id_utilisateur=%(id_utilisateur)", 
                           {
                            "id_utilisateur": collection.id_utilisateur,  
                            }                                
                        )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)

        liste_manga = []
        if res:
            for row in res:
                manga = MangaPhysique(
                    id_manga=row["id.manga"],
                    auteur=row["auteur"],
                    titre=row["titre"],
                    synopsis=row["synopsis"],
                    id_utilisateur=row["id_utilisateur"],
                    dernier_tome=row["num_dernier"],
                    tomes_manquants=row["num_manquants"],
                    status=row["status"],

                     ) 
                
                liste_manga.append(manga)
        
        return liste_manga 


    
    def liste_manga_virtuelle(self, collection) -> list:
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
                        f"WHERE cm.id_utilisateur=%(id_utilisateur)"
                        f"AND cm.titre_collec=%(titre)", 
                           {
                            "id_utilisateur": collection.id_utilisateur,
                            "titre":collection.titre  
                            }                                
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
