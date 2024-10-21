from src.buisness_objet.collection.abstract_collection import AbstractCollection 
from src.buisness_objet.manga_Physique import mangaPhysique 
from src.buisness_objet.manga import manga     


class CollectionPhysique(AbstractCollection):

    def __init__(self, titre, id_utilisateur, list_manga):
        for i in list_manga:
            if not isinstance(i, mangaPhysique):
                super().__init__(titre, id_utilisateur, list_manga)
                self.type = "physique"
                
    def __eq__(self, autre_collection):
        return (self.titre == autre_collection.titre and 
                self.id_utilisateur == autre_collection.id_utilisateur and 
                self.list_manga == autre_collection.liste_manga and 
                self.type == autre_collection.type)

    def ajouter_manga(self, new_manga: manga, liste_tome: list):
        if isinstance(new_manga, mangaPhysique):
            for i in liste_tome:
                if isinstance(i, int):
                    self.list_manga.append({"manga": new_manga, "tomes": liste_tome_manquant})

    def supprimer_manga(self, manga):
        for i in self.list_manga:
            if i.manga == manga:
                self.list_manga.remove(i)
