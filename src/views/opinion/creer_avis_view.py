from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.avis_service import AvisService
from src.service.manga_service import MangaService
from src.views.session import Session
from src.views.users.main_opinion_view import MainOpinionView


class CreateOpinionView(AbstractView):
    """Menu principal des avis"""

    def choisir_menu(self):
        """Choix du menu suivant

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        titre_manga = inquirer.text(
            "Entrez le nom du manga sur lequel vous voulez" " partager votre avis :)"
        ).execute()
        try:
            manga = MangaService().rechercher_un_manga(titre_manga=titre_manga)
        except Exception as e:
            print("\n", e, "\n")
            return MainOpinionView(
                "\n" + "=" * 50 + " Menu des avis" " :) " + "=" * 50 + "\n"
            )

        id_manga = manga.id_manga
        user = Session().getuser()
        id_utilisateur = user.id_utilisateur

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Rédiger un avis",
                "Donner une note",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Rédiger un avis":
                texte = inquirer.text("Rédigez votre avis :)").execute()

                spoiler = inquirer.select(
                    message="Cet avis contient-il un spoiler ?", choices=["Oui", "Non"]
                ).execute()

                # Convertir la réponse en un booléen
                spoiler = spoiler == "Oui"

                try:
                    AvisService().creer(
                        id_manga=id_manga,
                        id_utilisateur=id_utilisateur,
                        texte=texte,
                        spoiler=spoiler,
                    )  # Passer l'argument spoiler
                except Exception as e:
                    print("\n", e, "\n")

                return MainOpinionView(
                    "\n" + "=" * 50 + " Menu des avis" " :) " + "=" * 50 + "\n"
                )

            case "Donner une note":
                note = int(
                    inquirer.number(
                        f"Donnez votre note à {manga.titre_manga}",
                        min_allowed=0,
                        max_allowed=5,
                    ).execute()
                )
                try:
                    AvisService().noter(
                        id_manga=id_manga, id_utilisateur=id_utilisateur, note=note
                    )
                except Exception as e:
                    print("\n", e, "\n")

                return MainOpinionView(
                    "\n" + "=" * 50 + " Menu des avis" " :) " + "=" * 50 + "\n"
                )

            case "Retour":
                return MainOpinionView(
                    "\n" + "=" * 50 + " Menu des avis" " :) " + "=" * 50 + "\n"
                )
