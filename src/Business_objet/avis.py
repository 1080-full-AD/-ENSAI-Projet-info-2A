class Avis:
    """Classe représentant un avis

     Attributs
    ----------
    id_manga : int
        identifiant du manga
    id_utilisateur : int
        identifiant de l'utilisateur
    avis: str
        l'avis de l'utilisateur
    """
    def __init__(self, id_manga, id_utilisateur, avis):
        """Constructeur"""
        self.id_manga = id_manga
        self.id_utilisateur = id_utilisateur
        self.avis = avis

    def ajoute_avis(self, id_manga, id_utilisateur, avis):
        """Ajouter un nouvel avis à l'objet.

        Parameters
        ----------
        id_manga : int
            L'identifiant du manga
        id_utilisateur : int
            L'identifiant de l'utilisateur
        avis : str
            Le contenu de l'avis
        """
        self.id_manga = id_manga
        self.id_utilisateur = id_utilisateur
        self.avis = avis
        print(f"Avis ajouté: {self}")

    def supprimer_avis(self):
        """Supprimer un avis."""
        self.id_manga = None
        self.id_utilisateur = None
        self.avis = None
        print("Avis supprimé.")

    def modifier_avis(self, avis):
        """Modifier l'avis.

        Parameters
        ----------
        avis : str
            Le nouveau contenu de l'avis
        """
        if self.avis is not None:
            self.avis = avis
            print(f"Avis modifié: {self}")
        else:
            print("Aucun avis à modifier.")       