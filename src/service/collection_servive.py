from src.business_objet.collection.collection_virtuelle import CollectionVirtuelle
from src.dao.collection_dao import CollectionDao
from src.utils.log_decorator import log 
from src.business_objet.manga_physique import MangaPhysique
from src.business_objet.manga import Manga


class CollectionVirtuelleService:
    "classe contenant les services des collections virtuelles"

    @log
    def creer(self, titre, id_utilisateur, list_manga)-> CollectionVirtuelle:
        "création d'une collection virtuelle a partir de ses attributs"

        if not all(isinstance(i, Manga) for i in list_manga) :
            raise ValueError("les collections virtuelles ne conteniennent que des mangas virtuelles")

        for i in list_manga:
            if isinstance(i , MangaPhysique):
                raise ValueError("les collection virtuelles ne peuvent contenir des collections physique")
                break

        nouvelle_collection = CollectionVirtuelle(    
            titre=titre,
            id_utilisateur=id_utilisateur,
            list_manga=list_manga,
            )

        if CollectionDao().creer(nouvelle_collection) and all(CollectionDao().ajouter_collection_virtuelle(manga) for manga in list_manga):
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

        return CollectionDao().supprimer(collection)


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
        if new_manga in CollectionDao().liste_manga_virtuelle(collection):
            raise ValueErrror("ce manga appartient déja à cette collection")
        return CollectionDao().ajouter_collection_virtuelle(new_manga)


    @log    
    def supprimer_manga(self,collection, manga):
        if manga not in CollectionDao().liste_manga_virtuelle(collection):
            raise ValueError("ce manga ne fait pas partir de cette collection")
        else :
            return CollectionDao().supprimer_manga_virtuel(manga)
       


class CollectionPhysiqueService:
    "classe contenant les services des collections physique"