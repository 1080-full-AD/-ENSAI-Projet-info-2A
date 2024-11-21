from src.business_objet.collection_virtuelle import CollectionVirtuelle
from src.dao.collection_dao import CollectionDao
from src.utils.log_decorator import log 
from src.business_objet.manga_physique import MangaPhysique
from src.business_objet.manga import Manga


class CollectionVirtuelleService:
    "classe contenant les services des collections virtuelles"

    @log
    def creer(self, titre: str, id_utilisateur: int, liste_manga: list[Manga], description: str)-> CollectionVirtuelle:
        "création d'une collection virtuelle a partir de ses attributs"

        if not all(isinstance(i, Manga) for i in liste_manga) :
            raise ValueError("Les collections virtuelles ne conteniennent que des mangas virtuelles :/")

        for i in liste_manga:
            if isinstance(i, MangaPhysique):
                raise ValueError("les collection virtuelles ne peuvent contenir des mangas physique")

        if CollectionDao().titre_existant(titre=titre, id_utilisateur=id_utilisateur)== True:
            raise ValueError("Vous avez déja une collection avec ce titre :/")

        nouvelle_collection = CollectionVirtuelle(
            titre=titre,
            id_utilisateur=id_utilisateur,
            liste_manga=liste_manga,
            description=description
            )

        if CollectionDao().creer(
            collection=nouvelle_collection
            ) and all(CollectionDao().ajouter_manga(collection=nouvelle_collection , manga=manga) for manga in liste_manga):
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

        return CollectionDao().supprimer_collection(collection)


    @log
    def liste_manga(self, collection):
        "lister tous les mangas qui composent la collection"
        return CollectionDao().liste_manga(collection)


    @log 
    def ajouter_manga(self, collection, new_manga):
        if not isinstance(new_manga, Manga):
            raise ValueError(f"{new_manga} n'est pas un manga")
        if isinstance(new_manga, MangaPhysique):
            raise ValueError("les collections virtuelle ne contiennent que des mangas virtuelles")
        if new_manga in CollectionDao().liste_manga(collection):
            raise ValueError(f"Ce manga appartient déja à {collection.titre} :/")
        return CollectionDao().ajouter_manga(collection=collection,manga=new_manga)


    @log    
    def supprimer_manga(self,collection, manga):
        if manga not in CollectionDao().liste_manga(collection):
            raise ValueError("ce manga ne fait pas partir de cette collection")
        else :
            return CollectionDao().supprimer_manga(manga= manga, collection= collection)
