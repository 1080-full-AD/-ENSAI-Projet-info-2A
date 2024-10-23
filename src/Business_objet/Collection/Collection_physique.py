
from src.business_objet.collection.abstract_collection import AbstractCollection 
from src.business_objet.manga_physique import MangaPhysique 
from src.business_objet.manga import Manga     


class CollectionPhysique(AbstractCollection):

    def __init__(self, id_collection, titre, id_utilisateur, list_manga):
        if not all(isinstance(i, MangaPhysique) for i in list_manga):
            raise ValueError("les mangas doivent être des mangas physiques.")

        super().__init__(id_collection, titre, id_utilisateur, list_manga) 
        self.type = "physique"
                
    def __eq__(self, autre_collection):
        return (self.titre == autre_collection.titre and 
                self.id_utilisateur == autre_collection.id_utilisateur and 
                self.list_manga == autre_collection.liste_manga and 
                self.type == autre_collection.type)

    def ajouter_manga(self, new_manga: Manga):
        if not isinstance(new_manga, MangaPhysique):
            raise TypeError(f"{new_manga} n'est pas un manga physique")
        self.list_manga.append(new_manga)

    def supprimer_manga(self, manga):
        if manga not in self.list_manga:
            raise TypeError("ce manga n'est pas dans cette collection")

        self.list_manga.remove(manga)
                
    


