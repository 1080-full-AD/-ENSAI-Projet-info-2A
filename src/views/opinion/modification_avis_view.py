from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.avis_service import AvisService
from src.service.manga_service import MangaService
from src.views.session import Session


class ModificationAvisView(AbstractView):
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
            " modifier votre avis :)"
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
                f"Modifier l'avis",
                f"Modifier la note",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Modifier l'avis":
                texte = inquirer.text(
                    f"Rédigez votre nouvel avis  sur {manga.titre_manga}:)"
                ).execute()

                AvisService().creer(id_manga=id_manga,
                                    id_utilisateur=id_utilisateur, texte=texte)
                from src.views.users.main_opinion_view import MainOpinionView

                return MainOpinionView("\n" + "=" * 50 + " Menu des avis"
                                       " :) " + "=" * 50 + "\n")
            case "Modifier la note":

                note = int(inquirer.number(
                    f"Donnez votre nouvelle note à {manga.titre_manga} :)",
                    min_allowed=0,
                    max_allowed=5
                ).execute())
                AvisService().modifier_note(id_manga=id_manga,
                                    id_utilisateur=id_utilisateur, newnote=note)

                from src.views.users.main_opinion_view import MainOpinionView

                return MainOpinionView("\n" + "=" * 50 + " Menu des avis"
                                       " :) " + "=" * 50 + "\n")

            case "Retour":
                from src.views.users.main_opinion_view import MainOpinionView

                return MainOpinionView("\n" + "=" * 50 + " Menu des avis"
                                       " :) " + "=" * 50 + "\n")
