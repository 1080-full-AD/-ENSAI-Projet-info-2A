from src.utils.singleton import Singleton
from src.business_objet.utilisateur import Utilisateur
from src.dao.utilisateur_dao import UtilisateurDao
from src.utils.log_decorator import log
from src.utils.securite import hash_password
import re


class UtilisateurService(metaclass=Singleton):
    """"Classe exposant les méthodes liées à l'utilisateur"""

    @log
    def pseudo_deja_utilise(self, pseudo) -> bool:
        """Vérifie si le pseudo est déjà utilisé
        Retourne True si le pseudo existe déjà en BDD"""
        utilisateur = self.UtilisateurDao.lister_tous()
        return pseudo in [j.pseudo for j in utilisateur]

    @log
    def creer_utilisateur(self, pseudo, age, mdp=None, collections=[],
                          id_utilisateur=None) -> Utilisateur:
        """Création d'un utilisateur à partir de ses attributs"""
        if len(pseudo) == 0:
            raise ValueError("Le nom d'utilisateur ne peut pas être vide.")
        if not isinstance(pseudo, (str, int)):
            raise TypeError("Le nom d'utilisateur doit être une chaîne de" 
                            "caractères et/ou d'entiers")
        pseudo = str(pseudo)
        if self.pseudo_deja_utilise(pseudo):
            raise ValueError("Ce nom d'utilisateur est dèjà pris.")
        self.is_valid_mdp(mdp)
        self.UtilisateurDao.creer()
        print(f"Compte créé avec succès pour l'utilisateur : {pseudo}")

        nouvel_utilisateur = Utilisateur(
            pseudo=pseudo,
            age=age,
            mdp=hash_password(mdp, pseudo),
            collections=collections,
            id_utilisateur=id_utilisateur,
        )
        if self.UtilisateurDao.creer(nouvel_utilisateur):
            return nouvel_utilisateur
        else:
            return None

    @log
    def modifier_utilisateur(self, utilisateur) -> Utilisateur:
        """Modification d'un utilisateur"""
        utilisateur.mdp = hash_password(utilisateur.mdp, utilisateur.pseudo)
        return utilisateur if self.UtilisateurDao.modifier(utilisateur) else None

    @log
    def supprimer_utilisateur(self, utlisateur) -> bool:
        """Supprimer le compte d'un utilisateur"""
        return self.UtilisateurDao.supprimer(utlisateur)
    
    @log
    def lister_tous_utilisateur(self, inclure_mdp=False) -> list[Utilisateur]:
        """Lister tous les utilisateurs
        Si inclure_mdp=True, les mots de passe seront inclus
        Par défaut, tous les mdp des utilisateurs sont à None
        """
        utilisateur = self.UtilisateurDao.lister_tous()
        if not inclure_mdp:
            for j in utilisateur:
                j.mdp = None
        return utilisateur

    @log
    def trouver_par_pseudo_utilisateur(self, pseudo) -> Utilisateur:
        """Trouver un utilisateur à partir de son pseudo"""
        return self.UtilisateurDao.trouver_par_pseudo(pseudo)

    @log
    def se_connecter(self, pseudo, mdp) -> Utilisateur:
        """Se connecter à partir de pseudo et mdp"""
        return self.UtilisateurDao.se_connecter(pseudo,
                                             hash_password(mdp, pseudo))
    
    @log
    def se_deconnecter(self) -> Utilisateur:
        """Se déconnecter de l'application"""
        if self.pseudo:
            print(f"{self.pseudo} se déconnecte.")
            self.pseudo = None
        else:
            print("Aucun utilisateur n'est connecté.")
    
    def create_password(self):
        """Demande à l'utilsateur de créer un mot de passe"""
        mdp = input("Veuillez créer un mot de passe :")
        if self.is_valid_mdp(mdp):
            self.mdp = mdp
            print("Mot de passe créer avec succès !")
        else:
            print("Le mot de passe ne respecte pas les critères suivants:")
            print("-Au moins 8 caractères")
            print("-Au moins une lettrre minuscule")
            print("-Au moins une lettre majuscule")
            print("-Au moins un chiffre")
            print("-Au moins un caractère spécial parmi les suivants: %, #, /")
            self.create_password()
 
    def is_valid_mdp(self, mdp):
        """Méthode permettant de vérifier si le mot de passe créé est valide"""
        try:
            if (len(mdp)) < 8:
                raise ValueError("Le mot de passe doit contenir au moins 8"
                                 "caractères.")
            if re.search(r"[A-Z]", mdp):
                raise ValueError("Le mot de passe doit contenir au moihns une"
                                 "majuscule.")
            if re.search(r"[a-z]", mdp):
                raise ValueError("Le mot de passe doit contenir au moins une"
                                 "minuscule.")
            if re.search(r"[0-9]", mdp):
                raise ValueError("Le mot de passe doit contenir au moins un"
                                 "chiffre.")
            if re.search(r"[%#/]", mdp):
                raise ValueError("Le mot de passe doit contenir au moins un"
                                 "caractère spécial parmi ceux-là")
        except (ValueError, TypeError) as e:
            print(f"Erreur : {e}")
