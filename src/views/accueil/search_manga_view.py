from InquirerPy import inquirer

from src.views.abstract_view import AbstractView

from src.views.accueil.main_menu_view import MainView
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
                id = inquirer.text(message="Entrez l'identifiant "
                                           "du manga :) ").execute()
                try:
                    MangaService().rechercher_un_id_manga(id)
                except Exception:
                    return MangaSearchView("L'identifiant doit "
                                           "être un entier :/")

            case "Nom":
                name = inquirer.text(message="Entrez le nom "
                                             "du manga :) ").execute()
                try:
                    MangaService().rechercher_un_manga(name)
                except Exception:
                    return MangaSearchView("Le nom doit être une "
                                           "chaine de caractère :/")

            case "Auteur":
                author = inquirer.text(message="Entrez le nom"
                                               "de l'auteur :) ").execute()
                try:
                    MangaService().rechercher_un_auteur(author)
                except Exception:
                    return MangaSearchView("Le nom de l'auteur doit être une "
                                           "chaine de caractère :/")
