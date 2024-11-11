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
    def __init__(self, id_manga, id_utilisateur, texte):
        """Constructeur"""
        self.id_manga = id_manga
        self.id_utilisateur = id_utilisateur
        self.texte = texte

    def __str__(self):
        return (
            f"Avis de l'utilisateur {self.id_utilisateur}"
            f" sur le manga {self.id_manga}:"
            f"\n {self.texte}"
        )
