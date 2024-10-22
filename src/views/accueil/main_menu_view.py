from InquirerPy import inquirer
from src.views.abstract_view import AbstractView


class MainView(AbstractView):
    """Vue d'accueil de l'application"""

    def choisir_menu(self):
        """Choix du menu suivant

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "=" * 50 + " Menu principal " + "=" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Se connecter",
                "Créer un compte",
                "Rechercher des mangas",
                "Quitter",
            ],
        ).execute()

        match choix:
            case "Quitter":
                print("\n" + "=" * 50 + " A bientôt :) " + "=" * 50 + "\n")
                pass

            case "Se connecter":
                from src.views.accueil.connexion_view import ConnexionView

                return ConnexionView("\n" + "=" * 50 + "Connexion "
                                     "à l'application" + "=" * 50 + "\n")

            case "Créer un compte":
                from src.views.accueil.create_account import RegistrationWiew

                return RegistrationWiew("\n" + "=" * 50 + " Création"
                                        " de compte " + "=" * 50 + "\n")

            case "Rechercher des mangas":
                from src.views.manga_search import MangaSearch

                return MangaSearch("\n" + "=" * 50 + " Recherche"
                                   " de mangas " + "=" * 50 + "\n")
