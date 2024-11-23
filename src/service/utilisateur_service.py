from src.utils.singleton import Singleton
from src.business_objet.utilisateur import Utilisateur
from src.dao.utilisateur_dao import UtilisateurDao
from src.utils.log_decorator import log
from src.utils.securite import hash_password
from src.views.session import Session
import re


class UtilisateurService(metaclass=Singleton):
    """ "Classe exposant les méthodes liées à l'utilisateur"""

    @log
    def pseudo_deja_utilise(self, pseudo) -> bool:
        """Vérifie si le pseudo est déjà utilisé
        Retourne True si le pseudo existe déjà en BDD

        Parameters
        ----------
        pseudo : str
            pseudo de l'utilisateur

        Returns
        ----------
            bool
                True si le pseudo est déjà utilisé par un utilisateur
                False sinon
        """
        utilisateur = UtilisateurDao().lister_tous()
        return pseudo in [j.pseudo for j in utilisateur]

    @log
    def creer_utilisateur(
        self, pseudo, age, mot_de_passe=None, id_utilisateur=None, is_admin=False
    ) -> Utilisateur:
        """Création d'un utilisateur à partir de ses attributs

        Parameters
        ----------
        pseudo : str
            pseudo de l'utilisateur
        age : str
            age de l'utilisateur
        mot_de_passe : None
            par défaut
        id_utilisateur : None
            par défaut

        Returns
        ----------
        nouvel_ulisateur : list[Utilisateur]
                Si l'utilisateur est bien créé
                None sinon
        """
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
            is_admin=is_admin
        )
        if UtilisateurDao().creer(nouvel_utilisateur):
            return nouvel_utilisateur
        else:
            return None

    @log
    def modifier_utilisateur(self, utilisateur) -> Utilisateur:
        """Modification d'un utilisateur

        Parameters
        ----------
        utilisateur : Utilisateur

        Returns
        ----------
        utilisateur : Utilisateur
                Si l'utilisateur est bien modifié
                None sinon
        """
        utilisateur.mot_de_passe = hash_password(
            utilisateur.mot_de_passe, utilisateur.pseudo
        )
        if UtilisateurDao().modifier(utilisateur):
            return utilisateur
        else:
            None

    @log
    def supprimer_utilisateur(self, utilisateur) -> bool:
        """Supprimer le compte d'un utilisateur

        Parameters
        ----------
        utilisateur: Utilisateur

        Returns
        ----------
        utilisateur : Utilisateur
                Si l'utilisateur est bien supprimé
                None sinon
        """
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
        if isinstance(pseudo, str) is False:
            raise TypeError("Le pseudo doit être une chaîne de caractère :/")
        if UtilisateurDao().trouver_par_pseudo(pseudo) is None:
            print("Auncun utilisateur ne possède ce pseudo :/")
            return None
        else:
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
        Session().deconnexion()
        return None

    def create_password(self, mot_de_passe):
        """Demande à l'utilisateur de créer un mot de passe"""
        mot_de_passe = input("Veuillez créer un mot de passe :")
        if self.is_valid_mdp(mot_de_passe):
            self.mot_de_passe = mot_de_passe
            print("Mot de passe créé avec succès !")
        else:
            print("Le mot de passe ne respecte pas les critères suivants:")
            print("-Au moins 8 caractères")
            print("-Au moins une lettrre minuscule")
            print("-Au moins une lettre majuscule")
            print("-Au moins un chiffre")
            mot_de_passe = input("Veuillez créer un mot de passe :")
            self.create_password(mot_de_passe)

    def is_valid_mdp(self, mot_de_passe) -> bool:
        """Méthode permettant de vérifier si le mot de passe créé est valide"""
        if (len(mot_de_passe)) < 8:
            return False
        if not re.search(r"[A-Z]", mot_de_passe):
            return False
        if not re.search(r"[a-z]", mot_de_passe):
            return False
        if not re.search(r"[0-9]", mot_de_passe):
            return False
        return True
