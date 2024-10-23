class Utilisateur:
    """
    Classe représentant un Utilisateur

    Attributs
    ----------
    id_utilisateur : int
        identifiant
    pseudo : str
        pseudo du joueur
    mdp : str
        le mot de passe du joueur
    age : int
        age du joueur
    collections : list[Collection]
        liste de collections de mangas du joueur

    """

    def __init__(self, pseudo, age, mdp=None, id_utilisateur=None):
        """Constructeur"""
        self.id_utilisateur = id_utilisateur
        self.pseudo = pseudo
        self.mdp = mdp
        self.age = age

    def get_pseudo(self) -> str:
        """Permet d'afficher le pseudo de l'utilisateur"""
        return f"Joueur({self.pseudo}.)"
