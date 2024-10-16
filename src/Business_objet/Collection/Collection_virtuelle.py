from Buisness_objet.Collection.Abstract_Collection import AbstractCollection 
from Buisness_objet.manga import manga 


class CollectionVirtuelle(AbstractCollection):

    def __init__(self, titre, id_utilisateur, list_manga):
        for i in list_manga:
            if isinstance(i, manga) and not isinstance(i, mangaPhysique):
                super().__init__(titre, id_utilisateur, list_manga)
                self.type = "virtuelle"

    def Ajouter_manga(self, new_manga):
        if isinstance(new_manga, manga):
            self.list_manga.append(new_manga)

    def supprimer_manga(self, manga):
        if manga in self.list_manga:
            self.list_manga.remove(manga)
