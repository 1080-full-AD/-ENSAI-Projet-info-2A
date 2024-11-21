from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.avis_service import AvisService
from src.service.manga_service import MangaService
from src.views.session import Session
from src.views.users.main_opinion_view import MainOpinionView


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

        try:
            manga = MangaService().rechercher_un_manga(
                titre_manga=titre_manga
                )
        except Exception as e:
            print("\n", e, "\n")
            return MainOpinionView("\n" + "=" * 50 + " Menu des avis"
                                       " :) " + "=" * 50 + "\n")

        id_manga = manga.id_manga

        user = Session().getuser()
        id_utilisateur = user.id_utilisateur

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Modifier l'avis",
                "Modifier la note",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Modifier l'avis":
                texte = inquirer.text(
                    f"Rédigez votre nouvel avis  sur {manga.titre_manga} :)"
                ).execute()
                try:
                    AvisService().modifier(id_manga=id_manga,
                                        id_utilisateur=id_utilisateur,
                                        newtexte=texte)
                except Exception as e:
                    print("\n", e, "\n")

                return MainOpinionView("\n" + "=" * 50 + " Menu des avis"
                                        " :) " + "=" * 50 + "\n")

            case "Modifier la note":

                note = int(inquirer.number(
                    f"Donnez votre nouvelle note à {manga.titre_manga} :)"
                    " (entre 0 et 5)",
                    min_allowed=0,
                    max_allowed=5
                ).execute())
                try:
                    AvisService().modifier_note(id_manga=id_manga,
                                                id_utilisateur=id_utilisateur,
                                                newnote=note)
                except Exception as e:
                    print("\n", e, "\n")
               
                return MainOpinionView("\n" + "=" * 50 + " Menu des avis"
                                        " :) " + "=" * 50 + "\n")
            
            case "Retour":

                return MainOpinionView("\n" + "=" * 50 + " Menu des avis"
                                       " :) " + "=" * 50 + "\n")
