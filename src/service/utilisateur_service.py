from src.utils.singleton import Singleton
from src.business_objet.utilisateur import Utilisateur
from src.dao.utilisateur_dao import UtilisateurDao
from src.utils.log_decorator import log
from src.utils.securite import hash_password
import re


class UtilisateurService(metaclass=Singleton):
    """ "Classe exposant les méthodes liées à l'utilisateur"""

    @log
    def pseudo_deja_utilise(self, pseudo) -> bool:
        """Vérifie si le pseudo est déjà utilisé
        Retourne True si le pseudo existe déjà en BDD"""
        utilisateur = UtilisateurDao().lister_tous()
        return pseudo in [j.pseudo for j in utilisateur]

    @log
    def creer_utilisateur(
        self, pseudo, age, mot_de_passe=None, id_utilisateur=None
    ) -> Utilisateur:
        """Création d'un utilisateur à partir de ses attributs"""
        if len(pseudo) == 0:
            raise ValueError("Le nom d'utilisateur ne peut pas être vide.")
        if not isinstance(pseudo, (str, int)):
            raise TypeError(
                "Le nom d'utilisateur doit être une chaîne de"
                "caractères et/ou d'entiers"
            )
        pseudo = str(pseudo)
        if self.pseudo_deja_utilise(pseudo):
            raise ValueError("Ce nom d'utilisateur est déjà pris.")
        self.is_valid_mdp(mot_de_passe)

        nouvel_utilisateur = Utilisateur(
            pseudo=pseudo,
            age=age,
            mot_de_passe=hash_password(mot_de_passe, pseudo),
            id_utilisateur=id_utilisateur,
        )
        if UtilisateurDao().creer(nouvel_utilisateur):
            return nouvel_utilisateur
        else:
            return None

    @log
    def modifier_utilisateur(self, utilisateur) -> Utilisateur:
        """Modification d'un utilisateur"""
        utilisateur.mot_de_passe = hash_password(
            utilisateur.mot_de_passe, utilisateur.pseudo
        )
        if self.UtilisateurDao.modifier(utilisateur):
            return utilisateur
        else:
            None

    @log
    def supprimer_utilisateur(self, utilisateur) -> bool:
        """Supprimer le compte d'un utilisateur"""
        return UtilisateurDao().supprimer(utilisateur)

    @log
    def lister_tous_utilisateur(self, inclure_mdp=False) -> list[Utilisateur]:
        """Lister tous les utilisateurs
        Si inclure_mdp=True, les mots de passe seront inclus
        Par défaut, tous les mdp des utilisateurs sont à None
        """
        utilisateur = self.UtilisateurDao.lister_tous()
        if not inclure_mdp:
            for j in utilisateur:
                j.mot_de_passe = None
        return utilisateur

    @log
    def trouver_par_pseudo_utilisateur(self, pseudo) -> Utilisateur:
        """Trouver un utilisateur à partir de son pseudo"""
        return UtilisateurDao().trouver_par_pseudo(pseudo)

    @log
    def se_connecter(self, pseudo, mot_de_passe) -> Utilisateur:
        """Se connecter à partir de pseudo et mdp"""
        return UtilisateurDao().se_connecter(
            pseudo, hash_password(mot_de_passe, pseudo)
        )

    @log
    def se_deconnecter(self):
        """Se déconnecter de l'application"""
        return None

    def create_password(self):
        """Demande à l'utilsateur de créer un mot de passe"""
        mot_de_passe = input("Veuillez créer un mot de passe :")
        if self.is_valid_mdp(mot_de_passe):
            self.mot_de_passe = mot_de_passe
            print("Mot de passe créer avec succès !")
        else:
            print("Le mot de passe ne respecte pas les critères suivants:")
            print("-Au moins 8 caractères")
            print("-Au moins une lettrre minuscule")
            print("-Au moins une lettre majuscule")
            print("-Au moins un chiffre")
            self.create_password()

    def is_valid_mdp(self, mot_de_passe) -> bool:
        """Méthode permettant de vérifier si le mot de passe créé est valide"""
        if (len(mot_de_passe)) < 8:
            raise ValueError("Le mot de passe doit contenir au moins 8" "caractères.")
        if not re.search(r"[A-Z]", mot_de_passe):
            raise ValueError("Le mot de passe doit contenir au moins une" "majuscule.")
        if not re.search(r"[a-z]", mot_de_passe):
            raise ValueError("Le mot de passe doit contenir au moins une" "minuscule.")
        if not re.search(r"[0-9]", mot_de_passe):
            raise ValueError("Le mot de passe doit contenir au moins un" "chiffre.")
        else:
            return False
        return True
