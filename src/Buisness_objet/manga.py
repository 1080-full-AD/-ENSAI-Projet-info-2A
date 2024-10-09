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

    def __init__(self, id_manga, titre, auteur, synopsis):
        """Constructeur"""
        self.titre = titre
        self.id_manga = id_manga
        self.auteur = auteur
        self.synopsis = synopsis

    def trouve_titre(self, titre: str): Manga:
    """Permet d'afficher les informations du joueur"""
    if titre == Manga:
        return f"Manga({self.titre}, {self.auteur}, {self.synospsis})"
    else: 
        return None

