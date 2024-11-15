from src.business_objet.collection_virtuelle import CollectionVirtuelle
from src.dao.collection_dao import CollectionDao
from src.utils.log_decorator import log 
from src.business_objet.manga_physique import MangaPhysique
from src.business_objet.manga import Manga


class CollectionVirtuelleService:
    "classe contenant les services des collections virtuelles"

    @log
    def creer(self, collection)-> CollectionVirtuelle:
        "création d'une collection virtuelle a partir de ses attributs"

        if not all(isinstance(i, Manga) for i in collection.liste_manga) :
            raise ValueError("les collections virtuelles ne conteniennent que des mangas virtuelles")

        for i in collection.liste_manga:
            if isinstance(i , MangaPhysique):
                raise ValueError("les collection virtuelles ne peuvent contenir des collections physique")
                break

        nouvelle_collection = CollectionVirtuelle(    
            titre=collection.titre,
            id_utilisateur=collection.id_utilisateur,
            liste_manga=collection.liste_manga,
            description=collection.description
            )

        if CollectionDao().creer(nouvelle_collection) and all(CollectionDao().ajouter_manga(collection=nouvelle_collection , manga=manga) for manga in collection.liste_manga):
            return nouvelle_collection
        else:
            return None


    


    @log
    def modifier_collection(self , collection)->CollectionVirtuelle:
        "modifier une collection"
        return collection if CollectionDao().modifier(collection) else None




    @log
    def supprimer(self, collection) -> bool :
        "supprimer la collection de l'utilisateur"

        return CollectionDao().supprimer_collection_virtuelle(collection)


    @log
    def liste_manga(self, collection):
        "lister tous les mangas qui composent la collection"
        return CollectionDao().liste_manga(collection)


    @log 
    def ajouter_manga(self,collection,new_manga):
        if not isinstance(new_manga, Manga):
            raise ValueError(f"{new_manga} n'est pas un manga")
        if isinstance(new_manga, MangaPhysique):
            raise ValueError("les collections virtuelle ne contiennent que des mangas virtuelles")
        if new_manga in CollectionDao().liste_manga(collection):
            raise ValueErrror("ce manga appartient déja à cette collection")
        return CollectionDao().ajouter_manga(collection=collection,manga=new_manga)


    @log    
    def supprimer_manga(self,collection, manga):
        if manga not in CollectionDao().liste_manga(collection):
            raise ValueError("ce manga ne fait pas partir de cette collection")
        else :
            return CollectionDao().supprimer_manga_virtuel(manga)
       


class CollectionPhysiqueService:
    "classe contenant les services des collections physique"