from src.business_objet.manga import Manga 


class MangaPhysique(Manga):
    def __init__(self, id_manga, id_utilisateur, titre, auteur, synopsis, tomes_manquants, dernier_tome, status):
        super().__init__(id_manga, titre, auteur, synopsis)
        self.id_utilisateur = id_utilisateur
        self.tomes_manquants = tomes_manquants
        self.dernier_tome = dernier_tome
        self.status = status

    def liste_tome(self):
        liste_tome = [i for i in range(1,self.dernier_tome+1) if i not in self.tomes_manquants]
        return liste_tome

    def ajouter_tome(self, new_tome):
        if isinstance(new_tome, int):
            if new_tome in self.tomes_manquants:
                self.tomes_manquants.remove(new_tome)

            elif new_tome > self.dernier_tome:
                for i in range(1, new_tome-self.dernier_tome):
                    self.tomes_manquants.append(self.dernier_tome+i)
                    self.dernier_tome = new_tome

            else:
                print("tome deja existant")

    def enlever_tome(self, tome):
        if isinstance(tome, int):
            if tome == self.dernier_tome:
                dernier_tome = max(self.liste_tome.remove(self.dernier_tome))
                self.dernier_tome = dernier_tome
            
            elif tome < self.dernier_tome:
                self.tomes_manquants.append(tome)
            else:
                print("tome pas existant")


