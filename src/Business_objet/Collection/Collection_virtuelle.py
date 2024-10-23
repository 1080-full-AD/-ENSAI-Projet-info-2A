from src.business_objet.collection.abstract_collection import AbstractCollection 
from src.business_objet.manga import Manga 
from src.business_objet.manga_physique import MangaPhysique
=======
<<<<<<< HEAD
from src.buisness_objet.collection.abstract_collection import AbstractCollection 
=======
from src.buisness_objet.Collection.Abstract_Collection import AbstractCollection 
>>>>>>> ef78e09bda6c655c008d633f47ecede1ec99e587
from src.buisness_objet.manga import manga 
>>>>>>> 02ece90774e1be434f64af209eca5da38241a176


class CollectionVirtuelle(AbstractCollection):

    def __init__(self, id_collection, titre, id_utilisateur, list_manga):
        if not all(isinstance(i, Manga) for i in list_manga) :
            raise ValueError("les collections virtuelles ne conteniennent que des mangas virtuelles")
        for i in list_manga :
            if isinstance(i,MangaPhysique):
               raise ValueError("les collection virtuelles ne peuvent contenir des collections physique")
               break

        super().__init__(id_collection, titre, id_utilisateur, list_manga)
        self.type = "virtuelle"
    
    def ajouter_manga(self, new_manga):
        if not isinstance(new_manga, Manga):
            raise ValueError(f"{new_manga} n'est pas un manga")
        if isinstance(new_manga, MangaPhysique):
            raise ValueError("les collections virtuelle ne contiennent que des mangas virtuelles")
        self.list_manga.append(new_manga)

    def supprimer_manga(self, manga):
        if manga not in self.list_manga:
            raise ValueError("ce manga ne fait pas partir de cette collection")
        self.list_manga.remove(manga)
