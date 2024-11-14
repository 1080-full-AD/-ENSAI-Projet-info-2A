from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.utilisateur_service import UtilisateurService
from src.service.avis_service import AvisService
from src.service.manga_service import MangaService
from src.views.session import Session


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
                "Rédiger un avis/donner une note",
                "Modifier un avis/modifier une note",
                "Supprimer un avis/supprimer une note",
                "Consulter les avis/notes",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Rédiger un avis/donner une note":                
                from src.views.opinion.creer_avis_view import CreateOpinionView

                return CreateOpinionView("\n" + "=" * 50 + " Création d'avis"
                                         " :) " + "=" * 50 + "\n")

            case "Modifier un avis/modifier une note":
                pass

            case "Supprimer un avis/supprimer une note":
                pass

            case "Consulter les avis/notes":
                from src.views.opinion.consulter_avis_view import ConsulterAvisView

                return ConsulterAvisView("\n" + "=" * 50 + " Consultation d'avis"
                                         " :) " + "=" * 50 + "\n")
            case "Retour":
                from src.views.users.main_user_view import MainUserView


                return MainUserView("Retour au menu utilisateur :)")
