from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.utilisateur_service import UtilisateurService


class MainOpinionView(AbstractView):
    """Menu principal des avis"""

    def choisir_menu(self):
        """Choix du menu suivant

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Rédiger un avis",
                "Modifier un avis",
                "Supprimer un avis",
                "Consulter les avis",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Rédiger un avis":
                pass

            case "Modifier un avis":
                pass

            case "Supprimer un avis":
                pass

            case "Consulter les avis":
                from src.views.opinion.consulter_avis_view import ConsulterAvisView

                return ConsulterAvisView("\n" + "=" * 50 + " Consultation d'avis"
                            " :) " + "=" * 50 + "\n")
            case "Retour":
                from src.views.users.main_user_view import MainUserView

                return MainUserView("Retour au menu utilisateur :)")
