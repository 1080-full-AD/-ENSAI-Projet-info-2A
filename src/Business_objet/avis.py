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
    spoiler: bool
        si l'avis contient un spoiler ou pas
    """
    def __init__(self, id_manga, id_utilisateur, texte=None, note=None, spoiler =False):
        """Constructeur"""
        self.id_manga = id_manga
        self.id_utilisateur = id_utilisateur
        self.texte = texte
        self.note = note
        self.spoiler = spoiler

    def __str__(self):
        return (
            f"Avis de l'utilisateur {self.id_utilisateur}"
            f" sur le manga {self.id_manga}:"
            f"\n{self.texte}"
            "\n"
            f"\nNote donnée: {self.note}"
            "\n\n"
        )
