from InquirerPy import inquirer

from src.views.abstract_view import AbstractView

from src.views.accueil.main_menu import MainView
from src.service.manga_service import MangaService


class MangaSearchView(AbstractView):
    """Vue de recherche de mangas"""

    def choisir_menu(self):

        choix = inquirer.select(
            message="Quel est votre critère de recherche ?",
            choices=[
                "Identifiant",
                "Nom",
                "Auteur",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Retour":
                return MainView("Retour au menu princial :)")

            case "Identifiant":
                id = inquirer.text(message="Entrez l'identifiant"
                                           "du manga :) ").execute()
                MangaService()

            case "Nom":
                name = inquirer.text(message="Entrez le nom"
                                           "du manga :) ").execute()
                MangaService()

            case "Auteur":
                author = inquirer.text(message="Entrez le nom"
                                           "de l'auteur :) ").execute()
                MangaService()
