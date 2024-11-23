from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.avis_service import AvisService
from src.service.manga_service import MangaService
from src.views.session import Session
from src.views.users.main_opinion_view import MainOpinionView


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
            "Entrez le nom du manga pour lequel vous voulez" " supprimer votre avis :)"
        ).execute()
        try:
            manga = MangaService().rechercher_un_manga(titre_manga=titre_manga)
        except Exception as e:
            print("\n", e)
            return MainOpinionView(
                "\n" + "=" * 50 + " Menu des avis" " :) " + "=" * 50 + "\n"
            )

        id_manga = manga.id_manga

        user = Session().getuser()
        id_utilisateur = user.id_utilisateur

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Supprimer l'avis",
                "Supprimer la note",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Supprimer l'avis":
                try:
                    AvisService().supprimer_avis(
                        id_manga=id_manga, id_utilisateur=id_utilisateur
                    )
                except Exception as e:
                    print("\n", e)

                return MainOpinionView(
                    "\n" + "=" * 50 + " Menu des avis" " :) " + "=" * 50 + "\n"
                )

            case "Supprimer la note":
                try:
                    AvisService().supprimer_note(
                        id_manga=id_manga, id_utilisateur=id_utilisateur
                    )
                except Exception as e:
                    print("\n", e)

                return MainOpinionView(
                    "\n" + "=" * 50 + " Menu des avis" " :) " + "=" * 50 + "\n"
                )

            case "Retour":
                return MainOpinionView(
                    "\n" + "=" * 50 + " Menu des avis" " :) " + "=" * 50 + "\n"
                )
