from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.utilisateur_service import UtilisateurService
from src.business_objet.utilisateur import Utilisateur

class MainUserView(AbstractView):
    """Vue d'accueil des utilisateurs"""

    def choisir_menu(self):
        """Choix du menu suivant

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "=" * 50 + " Bienvenue :) " + "=" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Rechercher des mangas",
                "Accéder au menu des collections",
                "Accéder au menu des avis",
                "Se déconnecter",
                "Supprimer son compte :(",
            ],
        ).execute()

        match choix:
            case "Rechercher des mangas":
                from src.views.accueil.search_manga_view import MangaSearchView

                return MangaSearchView("\n" + "=" * 50 + " Recherche"
                                       " de mangas " + "=" * 50 + "\n")

            case "Accéder au menu des collections ":
                from src.views.usres.menu_collections_view \
                    import MenuCollectionsView

                return MenuCollectionsView("\n" + "=" * 50 + " Menu des "
                                           "collections " + "=" * 50 + "\n")

            """case "Accéder au menu des avis":
                from src.views.accueil.main_notice_view import No

                return RegistrationWiew("\n" + "=" * 50 + " Menu des "
                                        "avis " + "=" * 50 + "\n")"""

            case "Se déconnecter":
                from src.views.accueil.main_menu_view import MainView

                UtilisateurService().se_deconnecter()
                return MainView("Retour au menu principal")

            case "Supprimer son compte :(":
                from src.views.accueil.main_menu_view import MainView

                UtilisateurService().supprimer_utilisateur()
                return MainView("Retour au menu principal")
