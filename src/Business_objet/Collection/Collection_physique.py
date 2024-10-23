
from src.business_objet.collection.abstract_collection import AbstractCollection 
from src.business_objet.manga_physique import MangaPhysique 
from src.business_objet.manga import Manga     


class CollectionPhysique(AbstractCollection):

    def __init__(self, id_collection, titre, id_utilisateur, list_manga):
        if not all(isinstance(i, mangaPhysique) for i in list_manga):
            raise ValueError("les mangas doivent être des mangas physiques.")

        super().__init__(id_collection, titre, id_utilisateur, list_manga) 
        self.type = "physique"
                
    def __eq__(self, autre_collection):
        return (self.titre == autre_collection.titre and 
                self.id_utilisateur == autre_collection.id_utilisateur and 
                self.list_manga == autre_collection.liste_manga and 
                self.type == autre_collection.type)

    def ajouter_manga(self, new_manga: Manga, liste_tomes_manquants: list):
        if isinstance(new_manga, mangaPhysique):
            if all(isinstance(i, int) for i in liste_tomes_manquants):
                self.list_manga.append({"manga": new_manga,
                                        "tomes_manquants": liste_tomes_manquants})

    def supprimer_manga(self, manga):
        for i in self.list_manga:
            if i['manga'] == manga:
                self.list_manga.remove(i)
                break 

    


