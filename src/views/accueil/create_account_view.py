
from InquirerPy import inquirer
from InquirerPy.validator import PasswordValidator, EmptyInputValidator
from src.views.abstract_view import AbstractView
from src.service.utilisateur_service import UtilisateurService


class RegistrationView(AbstractView):
    def choisir_menu(self):

        pseudo = inquirer.text(message="Entrez votre pseudo : ",
                               validate=EmptyInputValidator(),).execute()

        mdp = inquirer.secret(
            message="Entrez votre mot de passe : ",
            validate=PasswordValidator(
                length=8,
                cap=True,
                number=True,
                message="Au moins 8 caractères, incluant une majuscule et"
                        "un chiffre",
            ),
        ).execute()

        age = inquirer.number(
            message="Entrez votre age : ",
            min_allowed=0,
            max_allowed=120,
            validate=EmptyInputValidator(),
        ).execute()

        joueur = UtilisateurService().creer_utilisateur(pseudo, mdp, age)
        if joueur:
            message = (
                f"Votre compte {joueur.pseudo} a été créé."
                f"Vous pouvez maintenant vous connecter :)")
            print("cestbon")

        message = "Erreur de connexion :/"
        "(pseudo ou mot de passe invalide)"

        from src.views.accueil.main_menu_view import MainView

        return MainView(message)
