from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.avis_service import AvisService
from src.service.manga_service import MangaService
from src.views.session import Session


class SupprimerAvisView(AbstractView):
    """Menu principal des avis"""

    def choisir_menu(self):
        """Choix du menu suivant

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        titre_manga = inquirer.text(
            "Entrez le nom du manga pour lequel vous voulez"
            " supprimer votre avis :)"
        ).execute()

        manga = MangaService().rechercher_un_manga(
            titre_manga=titre_manga
            )
        id_manga = manga.id_manga

        user = Session().getuser()
        id_utilisateur = user.id_utilisateur

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                f"Supprimer l'avis",
                f"Supprimer la note",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Supprimer l'avis":

                from src.views.users.main_opinion_view import MainOpinionView
                AvisService().supprimer_avis(id_manga=id_manga, id_utilisateur=id_utilisateur)

                return MainOpinionView("\n" + "=" * 50 + " Menu des avis"
                                       " :) " + "=" * 50 + "\n")

            case "Supprimer la note":

                from src.views.users.main_opinion_view import MainOpinionView
                #######################################A FINIR##############################################
                return MainOpinionView("\n" + "=" * 50 + " Menu des avis"
                                       " :) " + "=" * 50 + "\n")

            case "Retour":
                from src.views.users.main_opinion_view import MainOpinionView

                return MainOpinionView("\n" + "=" * 50 + " Menu des avis"
                                       " :) " + "=" * 50 + "\n")
