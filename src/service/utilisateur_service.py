from utils.singleton import Singleton
from src.business_objet.utilisateur import Utilisateur
from src.business_objet.dao import UtilisateurDao
from utils.log_decorator import log
from utils.securite import hash_password


class UtilisateurService(metaclass=Singleton):
    """"Classe exposant les méthodes liées à l'utilisateur"""

    @log
    def creer_utilisateur(self, pseudo, age, mdp=None, collection=[],
                          id_utilisateur=None) -> Utilisateur:
        """Création d'un utilisateur à partir de ses attributs"""

        nouvel_utilisateur = Utilisateur(
            pseudo=pseudo,
            age=age,
            mdp=hash_password(mdp, pseudo),
            collection=collection,
            id_utilsiateur=id_utilisateur,
        )
        if UtilisateurDao().creer(nouvel_utilisateur):
            return nouvel_utilisateur
        else:
            return None

    
    @log
    def modifier_utilisateur(self, utilisateur) -> Utilisateur:
        """Modification d'un utilisateur"""

        utilisateur.mdp = hash_password(utilisateur.mdp, utilisateur.pseudo)
        return utilisateur if UtilisateurDao().modifier(utilisateur) else None

    @log
    def supprimer_utilisateur(self, utlisateur) -> bool:
        """Supprimer le compte d'un utilisateur"""
        return UtilisateurDao().supprimer(utlisateur)
    
    
    @log
    def lister_tous(self, inclure_mdp=False) -> list[Utilisateur]:
        """Lister tous les utilisateurs
        Si inclure_mdp=True, les mots de passe seront inclus
        Par défaut, tous les mdp des utilisateurs sont à None
        """
        utilisateur = UtilisateurDao().lister_tous()
        if not inclure_mdp:
            for j in utilisateur:
                j.mdp = None
        return utilisateur

    @log
    def trouver_par_pseudo(self, pseudo)-> Utilisateur:
        """Trouver un utilisateur à partir de son pseudo"""
        return UtilisateurDao().trouver_par_pseudo(pseudo)
    
    

    

    

