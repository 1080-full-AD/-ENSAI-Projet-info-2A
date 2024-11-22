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
                        f"INSERT INTO projet.collection (Titre_collec,"
                        f" id_utilisateur,description) "
                        f" VALUES (%(titre)s, %(id_utilisateur)s "
                        f" ,%(description)s)"
                        f" RETURNING Titre_collec;",
                        {
                            "titre": collection.titre, 
                            "id_utilisateur": collection.id_utilisateur,
                            "description": collection.description
                            
                            }
                            )
                           
                    res = cursor.fetchone()
                
        except Exception as e:
            logging.error("Error creer collection: %s", e)

        if res:
            collection.titre = res["titre_collec"]
            created = True

        return created

    @log
    def ajouter_manga(self, collection: CollectionVirtuelle, manga: Manga)-> bool:

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

                        f" INSERT INTO projet.collection_manga(id_utilisateur,"
                        f" id_manga, titre_collec)  "
                        f" VALUES(%(id_utilisateur)s,%(id_manga)s,"
                        f" %(titre_collec)s)",
                        
                        
                        {
                            "id_utilisateur": collection.id_utilisateur,
                            "id_manga": manga.id_manga,
                            "titre_collec": collection.titre,
                        }
                    )
                res = cursor.rowcount
        except Exception as e:
            logging.error("Error ajouter collection: %s", e)

        return res == 1      

    @log
    def supprimer_manga(self, collection: CollectionVirtuelle, manga: Manga) -> bool:

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

                        f" DELETE FROM projet.collection_manga"
                        f" WHERE id_manga=%(id_manga)s "
                        f" AND id_utilisateur=%(id_utilisateur)s  "
                        f" AND titre_collec=%(titre)s",
                        
                        
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
                        f"DELETE FROM projet.collection_manga   "
                        f" WHERE titre_Collec = %(titre)s" 
                        f" AND id_utilisateur = %(id_utilisateur)s;"
                        f" DELETE FROM projet.collection  " 
                        f" WHERE titre_Collec = %(titre)s "
                        f" AND id_utilisateur = %(id_utilisateur)s;",
                        
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
                        f"  titre_collec = %(titre)s  ,    "
                        f"  id_utilisateur = %(id_utilisateur)s , "
                        f"  description = %(description)s        "
                        f"  WHERE titre_collec=%(titre)s "
                        f"  AND id_utilisateur = %(id_utilisateur)s", 
                           
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
                        f"select *     "
                        f" FROM projet.collection_manga cm     "
                        f" JOIN projet.manga m USING(id_manga)"
                        f" WHERE cm.id_utilisateur=%(id_utilisateur)s"
                        f" AND cm.titre_collec=%(titre)s", 
                        {
                            "id_utilisateur": id_utilisateur,
                            "titre": titre_collec 
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

    @log
    def titre_existant(self, collection: CollectionVirtuelle)-> bool:
        
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
                        f"  SELECT titre_collec    "
                        f"  FROM projet.collection     "
                        f"  WHERE id_utilisateur=%(id_utilisateur)s",
                         
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
        
        return titre in liste_titre_collec



    @log
    def liste_collection(self, id_utilisateur: int)-> list:
        
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
                        f"  SELECT *    "
                        f"  FROM projet.collection     "
                        f"  WHERE id_utilisateur=%(id_utilisateur)s",
                         
                        {  
                            "id_utilisateur": id_utilisateur
                        }                                
                        )
                    res = cursor.fetchall()
        except Exception as e:
            logging.error("Error lister manga: %s", e)

        liste_collection = []
        if res:
            for row in res:
                liste_mangas = self.liste_manga(
                            id_utilisateur=row["id_utilisateur"],
                            titre_collec=row["titre_collec"]
                            )
                collection = CollectionVirtuelle(
                    titre=row["titre_collec"],
                    id_utilisateur=row["id_utilisateur"],
                    liste_manga=liste_mangas,
                    description=row["description"]

                )
                liste_collection.append(collection)
        
        return liste_collection

