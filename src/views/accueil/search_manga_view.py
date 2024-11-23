from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator
from src.views.abstract_view import AbstractView
from src.business_objet.manga import Manga
from src.service.manga_service import MangaService
from src.views.session import Session


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
                if Session().getuser() is None:
                    from src.views.accueil.main_menu_view import MainView

                    return MainView("Retour au menu princial :)")
                from src.views.users.main_user_view import MainUserView

                return MainUserView("Retour au menu princial :)")
            case "Identifiant":
                id = int(
                    inquirer.number(
                        message="Entrez l'identifiant " "du manga :) ",
                        validate=EmptyInputValidator(),
                    ).execute()
                )

                try:
                    manga = MangaService().rechercher_un_id_manga(id)
                    print(manga.__str__())
                    return MangaSearchView(
                        "\n" + "=" * 50 + " Recherche" " de mangas " + "=" * 50 + "\n"
                    )
                except Exception as e:
                    return MangaSearchView(e)
            case "Nom":
                name = inquirer.text(message="Entrez le nom " "du manga :) ").execute()
                try:
                    manga = MangaService().rechercher_un_manga(name)
                    print(manga.__str__())
                    return MangaSearchView(
                        "\n" + "=" * 50 + " Recherche" " de mangas " + "=" * 50 + "\n"
                    )
                except Exception as e:
                    return MangaSearchView(e)

            case "Mangaka":
                author = inquirer.text(
                    message="Entrez le nom" " de l'auteur :) "
                ).execute()
                try:
                    manga = MangaService().rechercher_un_auteur(author)
                    for i in manga:
                        print(i.__str__())
                    return MangaSearchView(
                        "\n" + "=" * 50 + " Recherche" " de mangas " + "=" * 50 + "\n"
                    )
                except Exception as e:
                    return MangaSearchView(e)
