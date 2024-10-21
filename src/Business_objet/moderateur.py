from src.business_objet.utilisateur import Utilisateur
from src.dao.utilisateur_dao import UtilisateurDao


class Moderateur:
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

    def __init__(self, pseudo, age, mdp=None,
                 collections=[], id_utilisateur=None):
        """Constructeur"""
        super().__init__(pseudo=pseudo, age=age, mdp=mdp,
                         collections=collections,
                         id_utilisateur=id_utilisateur)

    
    def get_pseudo(self, id_utilisateur: int) -> str:

