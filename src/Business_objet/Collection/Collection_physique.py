from Buisness_objet.Collection.Abstract_Collection import AbstractCollection 
from Buisness_objet.manga import manga 


class CollectionPhysique(AbstractCollection):

    def __init__(self, titre, id_utilisateur, list_manga):
        for i in list_manga:
            if not isinstance(i, mangaPhysique):
                super().__init__(titre, id_utilisateur, list_manga)

    def ajouter_manga(self, new_manga, liste_tome):
        if isinstance(new_manga, mangaPhysique):
            for i in liste_tome:
                if isinstance(i,int):
                    self.list_manga.append({"manga": new_manga, "tomes": liste_tome})

    def supprimer_manga(self,manga):
        for i in self.list_manga:
            if manga in i.keys():
                self.list_manga.remove(i)
