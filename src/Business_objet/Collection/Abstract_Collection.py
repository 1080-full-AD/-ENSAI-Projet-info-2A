from abc import ABC, abstractmethod


class AbstractCollection(ABC):

    def __init__(self,titre, id_utilisateur, list_manga):

        self.titre = titre
        self.id_utilisateur = id_utilisateur
        self.list_manga = list_manga

    def get_utilisateur(self):
        return self.id_utilisateur

    def get_titre(self):
        return self.titre 

    def modifier_tire(self,nouveau_titre):
        self.titre=nouveau_titre

    @abstractmethod
    def ajouter_manga(self, new_manga):
        pass

    @abstractmethod
    def supprimer_manga(self, manga):
        pass

