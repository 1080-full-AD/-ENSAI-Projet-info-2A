from src.business_objet.manga import Manga 


class MangaPhysique(Manga):
    def __init__(self, id_manga, id_utilisateur, titre, auteur, synopsis, tomes_manquants, dernier_tome, status):
        super().__init__(id_manga, titre, auteur, synopsis)
        self.id_utilisateur = id_utilisateur
        self.tomes_manquants = tomes_manquants
        self.dernier_tome = dernier_tome
        self.status = status

    def liste_tome(self):
        if self.tomes_manquants is None:
            self.tomes_manquants = []
        liste_tome = [i for i in range(1,self.dernier_tome+1) if i not in self.tomes_manquants]
        return liste_tome

    def ajouter_tome(self, new_tome):
        if not isinstance(new_tome, int):
            raise TypeError("Le tome ajouté doit être un entier")
        if new_tome in self.tomes_manquants:
            self.tomes_manquants.remove(new_tome)

        elif new_tome > self.dernier_tome:
            for i in range(1, new_tome-self.dernier_tome):
                self.tomes_manquants.append(self.dernier_tome+i)
            self.dernier_tome = new_tome

        else:
            print("tome deja existant")

    def enlever_tome(self, tome):
        if not isinstance(tome, int):
            raise TypeError(f"{tome},n'est pas un tome")

        if tome == self.dernier_tome:
            self.tomes_manquants.append(tome)
            self.tomes_manquants.sort()  # Trier pour garantir l'ordre croissant
            
        # On cherche le nouveau dernier tome qui n'est pas manquant
            nouveau_dernier_tome = tome - 1
            while nouveau_dernier_tome in self.tomes_manquants and nouveau_dernier_tome > 0:
                nouveau_dernier_tome -= 1
            
            self.dernier_tome = nouveau_dernier_tome
            
        elif tome < self.dernier_tome:
            self.tomes_manquants.append(tome)
        else:
            print("tome pas existant")


