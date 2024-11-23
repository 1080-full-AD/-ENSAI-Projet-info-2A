from InquirerPy import inquirer
from src.views.abstract_view import AbstractView


class MainModerationView(AbstractView):
    """Menu principal des collections"""

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
                "Gestion de la base de manga",
                "Gestion des avis",
                "Gestion des utilisateurs",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Gestion de la base de manga":
                from src.views.moderation.moderation_manga_view import (
                    ModerationMangaView,
                )

                return ModerationMangaView(
                    "\n" + "=" * 50 + " Modération de manga" + "=" * 50 + "\n"
                )

            case "Gestion des avis":
                from src.views.moderation.moderation_avis_view import (
                    ModerationAvisView
                )

                return ModerationAvisView(
                    "\n" + "=" * 50 + " Modération des avis "
                    + "=" * 50 + "\n"
                )

            case "Gestion des utilisateurs":
                from src.views.moderation.moderation_utilisateur_view import (
                    ModerationUtilisateurView
                )

                return ModerationUtilisateurView(
                    "\n" + "=" * 50 + " Modération des utilisateurs"
                    + "=" * 50 + "\n"
                )

            case "Retour":
                from src.views.users.main_user_view import MainUserView

                return MainUserView("Retour au menu utilisateur :)")
