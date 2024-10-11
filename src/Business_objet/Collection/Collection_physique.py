from src.buisness_objet.collection.abstract_collection import AbstractCollection 
from Buisness_objet.manga import manga 
from Buisness_objet.manga_Physique import mangaPhysique 

class CollectionPhysique(AbstractCollection):

    def __init__(self, titre, id_utilisateur, list_manga):
        for i in list_manga:
            if not isinstance(i, mangaPhysique):
                super().__init__(titre, id_utilisateur, list_manga)
                self.type="physique"


    def ajouter_manga(self, new_manga:manga, liste_tome:list):
        if isinstance(new_manga, mangaPhysique):
            for i in liste_tome:
                if isinstance(i,int):
                    self.list_manga.append({"manga": new_manga, "tomes": liste_tomegit})

    def supprimer_manga(self,manga):
        for i in self.list_manga:
            if i.manga==manga:
                self.list_manga.remove(i)
