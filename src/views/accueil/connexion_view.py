from InquirerPy import inquirer

from src.views.abstract_view import AbstractView
from src.views.session import Session

from src.service.utilisateur_service import UtilisateurService


class ConnexionView(AbstractView):
    """Vue de Connexion (saisie de pseudo et mdp)"""

    def choisir_menu(self):

        pseudo = inquirer.text(message="Entrez votre pseudo : ").execute()
        mdp = inquirer.secret(message="Entrez votre mot de passe :").execute()

        joueur = UtilisateurService().se_connecter(pseudo, mdp)

        if joueur:
            message = f"Vous êtes connecté sous le pseudo {joueur.pseudo}"
            Session().connexion(joueur)

            from views.menu_joueur_vue import MenuJoueurVue

            return MenuJoueurVue(message)

        message = "Erreur de connexion :/ (pseudo ou mot de passe invalide)"
        from src.views.accueil.main_menu import MainView

        return MainView(message)
