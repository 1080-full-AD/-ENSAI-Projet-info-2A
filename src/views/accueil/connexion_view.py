from InquirerPy import inquirer

from src.views.abstract_view import AbstractView

from src.service.utilisateur_service import UtilisateurService
from src.business_objet.utilisateur import Utilisateur


class ConnexionView(AbstractView):
    """Vue de Connexion (saisie de pseudo et mdp)"""

    def choisir_menu(self):

        pseudo = inquirer.text(message="Entrez votre pseudo : ").execute()

        mdp = inquirer.secret(message="Entrez votre mot de passe :").execute()

        user = UtilisateurService().se_connecter(pseudo, mdp)

        if user:
            message = f"Vous êtes connecté sous le pseudo {user.pseudo}"

            from src.views.users.main_user_view import MainUserView

            return MainUserView(message)

        message = "Erreur de connexion :/\n(pseudo ou mot de passe invalide)"
        from src.views.accueil.main_menu_view import MainView

        return MainView(message)
