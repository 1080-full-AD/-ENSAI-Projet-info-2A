import logging
from src.utils.singleton import Singleton
from src.utils.log_decorator import log
from typing import Optional
import json 


from src.business_objet.manga_physique import MangaPhysique

from src.business_objet.manga import Manga
from src.business_objet.utilisateur import Utilisateur
from src.dao.db_connection import DBConnection

class MangaPhysiqueDao(metaclass=Singleton):
    def creer(self, manga ) -> bool:

        """Creation d'un manga physique dans la base de données

        Parameters
        ----------
        manga: manga physique
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
                        f" INSERT INTO projet.mangatheque (id_manga,"
                        f" id_utilisateur,num_dernier,num_manquants,status) "
                        f" VALUES (%(id_manga)s, %(id_utilisateur)s ,"
                        f" %(num_dernier)s,"
                        f" %(num_manquants)s,%(status)s) RETURNING id_manga ;" 
                        , 
                        
                        {
                            "id_manga": manga.id_manga, 
                            "id_utilisateur": manga.id_utilisateur,
                            "num_dernier": manga.dernier_tome,
                            "num_manquants": json.dumps(manga.tomes_manquants),
                            "status": manga.status,

                            
                            }
                            )
        
                    res = cursor.fetchone()
                
        except Exception as e:
            
            logging.error("Error creating manga_physique: %s", e)
        
        if res:
            created = True
        
        return created


    @log
    def supprimer_manga_physique(self, manga) :

        """supprimer un manga physique  d'une collection physique

        Parameters
        ----------
        manga:manga a ajouter à la collection
        
        Returns
        -------
        bool
        true si la suppression  du manga à été effectuée
        """
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:

                    cursor.execute(

                        f" DELETE FROM projet.mangatheque"
                        f" WHERE id_utilisateur=%(id_utilisateur)s  "
                        f" AND id_manga=%(id_manga)s",
                        
                        
                    {

                        "id_utilisateur": manga.id_utilisateur,
                        "id_manga": manga.id_manga,
                        
                    }
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.error("Error delete manga_physique: %s", e)
        return res == 1

    
    def modifier_manga_physique(self,manga):
        """modifier le manga physique dans la base de données

        Parameters
        ----------
        manga:manga 
        
        Returns
        -------
        bool
        true le tome a été ajouter 
    
        """


        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        f"UPDATE projet.mangatheque      "
                        f"  id_utilisateur = %(id_utilisateur)s       "
                        f"  id_manga = %(id_manga)s   "
                        f"  num_dernier = %(num_dernier)s                      "
                        f"  num_manquants=%(num_manquants)s           "
                        f"  status=%(status)s"
                        f"  where titre=%(titre)s and id_utilisateur=%(id_utilisateur)s", 
                           
                        {
                            "id_manga": manga.id_manga,
                            "id_utilisateur": manga.id_utlisateur,
                            "num_dernier": manga.dernier_tome,
                            "num_manquants": json.dumps(manga.tomes_manquants),
                            "status": manga.status
                        },
                    )

                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)

        return res == 1


    def liste_manga_physique(self, utilisateur: Utilisateur) -> list:
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
                        f"  select *     "
                        f"  from projet.mangatheque mt     "
                        f"  JOIN projet.manga m USING(id_manga)"
                        f"  WHERE mt.id_utilisateur=%(id_utilisateur)s", 
                           {
                            "id_utilisateur": utilisateur.id_utilisateur,  
                            }                                
                        )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)

        liste_manga = []
        if res:
            for row in res:
                manga = MangaPhysique(
                    id_manga=row["id_manga"],
                    auteurs=row["auteurs"],
                    titre_manga=row["titre_manga"],
                    synopsis=row["synopsis"],
                    id_utilisateur=row["id_utilisateur"],
                    dernier_tome=row["num_dernier"],
                    tomes_manquants=row["num_manquants"],
                    status=row["status"],

                     ) 
                
                liste_manga.append(manga)
        
        return liste_manga 


    

