from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.utilisateur_service import UtilisateurService
from src.views.users.main_moderation_view import MainModerationView


class ModerationUtilisateurView(AbstractView):
    """Menu principal des collections"""

    def choisir_menu(self):
        """Choix du menu suivant

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        try:
            id_utilisateur = int(
                inquirer.number(message="Entrez l'identifiant"
                                        " de l'utilisateur que vous"
                                        " voulez supprimer").execute()
            )
            utilisateur = UtilisateurService().trouver_par_id_utilisateur(id=id_utilisateur)

        except Exception as e:
            print("\n", e)
            return MainModerationView(
                        "\n" + "=" * 50 + " Menu de modération " + "=" * 50 + "\n"
                    )
        supp = inquirer.confirm(
            message=f"Confirmer la suppression "
                    f"de de l'utilisateur {id_utilisateur} ?"
        ).execute()

        if supp is True:
            UtilisateurService().supprimer_utilisateur(
                utilisateur=utilisateur
            )

        return MainModerationView(
                    "\n" + "=" * 50 + " Menu de modération " + "=" * 50 + "\n"
                )
