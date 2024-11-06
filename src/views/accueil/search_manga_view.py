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
                    return MangaSearchView("\n" + "=" * 50 + " Recherche"
                                           " de mangas " + "=" * 50 + "\n")
                except Exception as e:
                    return MangaSearchView(e)
            case "Nom":
                name = inquirer.text(message="Entrez le nom "
                                             "du manga :) ").execute()
                try:
                    MangaService().rechercher_un_manga(name)
                    return MangaSearchView("\n" + "=" * 50 + " Recherche"
                                           " de mangas " + "=" * 50 + "\n")
                except Exception as e:
                    return MangaSearchView(e)

            case "Mangaka":
                author = inquirer.text(message="Entrez le nom"
                                               "de l'auteur :) ").execute()
                try:
                    MangaService().rechercher_un_auteur(author)
                    return MangaSearchView("\n" + "=" * 50 + " Recherche"
                                           " de mangas " + "=" * 50 + "\n")
                except Exception:
                    return MangaSearchView(e)
