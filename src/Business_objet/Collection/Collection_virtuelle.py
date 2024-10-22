from src.buisness_objet.Collection.Abstract_Collection import AbstractCollection 
from src.buisness_objet.manga import manga 


class CollectionVirtuelle(AbstractCollection):

    def __init__(self, id_collection, titre, id_utilisateur, list_manga):
        if all(isinstance(i, Manga) and not isinstance(i, MangaPhysique) for i in list_manga):
                super().__init__(id_collection, titre, id_utilisateur, list_manga)
                self.type = "virtuelle"

        else:
            raise ValueError("les collections virtuelles ne peuvent contenir des mangas physiques")

              

    def Ajouter_manga(self, new_manga):
        if isinstance(new_manga, manga):
            self.list_manga.append(new_manga)

    def supprimer_manga(self, manga):
        if manga in self.list_manga:
            self.list_manga.remove(manga)
