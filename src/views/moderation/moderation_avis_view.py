from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.avis_service import AvisService
from src.views.users.main_moderation_view import MainModerationView


class ModerationAvisView(AbstractView):
    """Menu principal des collections"""

    def choisir_menu(self):
        """Choix du menu suivant

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        id_utilisateur = int(
            inquirer.number(message="Entrez l'identifiant de l'utilisateur").execute()
        )
        id_manga = int(
            inquirer.number(message="Entrez l'identifiant du manga").execute()
        )

        supp = inquirer.confirm(
            message=f"Confirmer la suppression de l'avis de l'utilisateur {id_utilisateur} sur le manga {id_manga} ?"
        ).execute()
        if supp is True:
            AvisService().supprimer_avis(
                id_manga=id_manga, id_utilisateur=id_utilisateur
            )

        return MainModerationView(
            "\n" + "=" * 50 + " Menu de modération " + "=" * 50 + "\n"
        )
