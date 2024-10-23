from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator
from src.views.abstract_view import AbstractView

from src.service.manga_service import MangaService


class MangaSearchView(AbstractView):
    """Vue de recherche de mangas"""

    def choisir_menu(self):

        choix = inquirer.select(
            message="Quel est votre critère de recherche ?",
            choices=[
                "Identifiant",
                "Nom",
                "Mangaka",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Retour":
                from src.views.accueil.main_menu_view import MainView

                return MainView("Retour au menu princial :)")

            case "Identifiant":
                id = int(inquirer.number(message="Entrez l'identifiant "
                                                 "du manga :) ",
                                         validate=EmptyInputValidator()
                                         ).execute())

                try:
                    MangaService().rechercher_un_id_manga(id)
                except Exception:
                    return MangaSearchView("L'id doit être un "
                                           "entier :/")
            case "Nom":
                name = inquirer.text(message="Entrez le nom "
                                             "du manga :) ").execute()
                try:
                    MangaService().rechercher_un_manga(name)
                except Exception:
                    return MangaSearchView("Le nom doit être une "
                                           "chaine de caractère :/")

            case "Mangaka":
                author = inquirer.text(message="Entrez le nom"
                                               "de l'auteur :) ").execute()
                try:
                    MangaService().rechercher_un_auteur(author)
                except Exception:
                    return MangaSearchView("Le nom de l doit être une "
                                           "chaine de caractère :/")
