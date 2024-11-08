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

    def __str__(self):
        return (
            f"\n ---> {self.titre_manga}\n"
            f"      Identifiant: {self.id_manga}\n"
            f"      Auteur(s): {self.auteurs}\n"
            f"      Synopsis: {self.synopsis}"
        )
