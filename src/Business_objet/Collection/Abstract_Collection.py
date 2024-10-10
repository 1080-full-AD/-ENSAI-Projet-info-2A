from abc import ABC, abstractmethod

class AbstractCollection(ABC):

    def __init__(
        titre:str,
        id_utilisateur:str,
        list_manga:list[Manga],
        ):

        self.titre=titre
        self.id_utilisateur=id_utilisateur
        self.list_manga=list_manga


    def get_utilisateur(self):
        return self.id_utilisateur


    def get_titre(self):
        return self.titre 


