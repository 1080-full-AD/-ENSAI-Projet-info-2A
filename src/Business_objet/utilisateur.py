class Utilisateur:
    """
    Classe représentant un Utilisateur

    Attributs
    ----------
    id_utilisateur : int
        identifiant
    pseudo : str
        pseudo de l'utilisateur
    mot_de_passe : str
        le mot de passe de l'utilisateur
    age : int
        age de l'utilisateur

    """

    def __init__(self, pseudo, age, mot_de_passe=None, id_utilisateur=None, is_admin=False):
        """Constructeur"""
        self.id_utilisateur = id_utilisateur
        self.pseudo = pseudo
        self.mot_de_passe = mot_de_passe
        self.age = age
        self.is_admin = is_admin

    def get_pseudo(self) -> str:
        """Permet d'afficher le pseudo de l'utilisateur"""
        return f"Utilisateur({self.pseudo}.)"
