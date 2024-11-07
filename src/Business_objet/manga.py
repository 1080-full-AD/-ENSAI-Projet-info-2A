class Manga:
    """Classe représentant un Manga

     Attributs
    ----------
    id_manga : str
        identifiant
    titre : str
        titre du manga
    auteur: str
        l'auteur du manga
    synopsis : int
        synopsis du manga
    """

    def __init__(self, id_manga, titre_manga, auteurs, synopsis):
        """Constructeur"""
        self.titre_manga = titre_manga
        self.id_manga = id_manga
        self.auteurs = auteurs
        self.synopsis = synopsis

    def trouve_titre(self, titre_manga: str):
        """Permet d'afficher les informations du joueur"""
        if titre_manga == Manga:
            return f"Manga({self.titre_manga}, {self.auteur}, {self.synospsis})"
        else:
            return None
