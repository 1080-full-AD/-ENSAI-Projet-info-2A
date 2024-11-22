
class CollectionVirtuelle:

    def __init__(self, titre, id_utilisateur, liste_manga, description):

        self.titre = titre
        self.id_utilisateur = id_utilisateur
        self.liste_manga = liste_manga
        self.description = description
    
    def __str__(self):
        L = [i.titre_manga for i in self.liste_manga]
        return (
            f"=== {self.titre} ===\n"
            f"Description: {self.description}\n"
            f"->{L}\n \n"
        )
