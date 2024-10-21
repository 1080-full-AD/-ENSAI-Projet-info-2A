from InquirerPy import inquirer
from src.views.vue_abstraite import AbstractView


class MainView(AbstractView):
    """Vue d'accueil de l'application"""

    def choisir_menu(self):
        """Choix du menu suivant

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\Bienvenue :)\n" + "-" * 50 + "\n")

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
                pass

            case "Se connecter":
                from src.views.accueil.connexion_vue import ConnexionVue

                return ConnexionVue("Connexion à l'application")

            case "Créer un compte":
                from src.views.accueil.inscription_vue import InscriptionVue

                return InscriptionVue("Création de compte joueur")

            case "Rechercher des mangas":
                from src.views.manga_search import MangaSearch
