from src.business_objet.manga import Manga 


class MangaPhysique(Manga):
    def __init__(self, id_manga, id_utilisateur, titre_manga, auteurs, synopsis , tomes_manquants, dernier_tome, status):
        super().__init__(id_manga, titre_manga, auteurs, synopsis)
        self.id_utilisateur = id_utilisateur
        self.tomes_manquants = tomes_manquants
        self.dernier_tome = dernier_tome
        self.status = status

    def liste_tome(self):
        if self.tomes_manquants is None:
            self.tomes_manquants = []
        liste_tome = [i for i in range(1,self.dernier_tome+1) if i not in self.tomes_manquants]
        return liste_tome

    

    