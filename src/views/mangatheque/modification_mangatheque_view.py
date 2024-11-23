from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.manga_physique_service import MangaPhysiqueService
from src.service.manga_service import MangaService
from src.views.session import Session
from src.views.users.main_mangatheque_view import MainMangathequeView


class ModificationMangathequeView(AbstractView):
    """Menu principal des avis"""

    def choisir_menu(self):
        """Choix du menu suivant

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        titre = inquirer.text(
            message="Donnez le titre de la mangathèque que"
            " vous souhaitez modifier :)",
        ).execute()

        try:
            manga = MangaService().rechercher_un_manga(titre_manga=titre)

            user = Session().getuser()
            id_utilisateur = user.id_utilisateur

            L = MangaPhysiqueService().rechercher_manga_physique(
                id_utilisateur=id_utilisateur, id_manga=manga.id_manga)

        except Exception as e:
            print("\n", e)
            return ModificationMangathequeView(
                "\n" + "=" * 50 + " Menu des mangathèques"
                " :) " + "=" * 50 + "\n"
            )

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Ajouter un tome",
                "Enlever un tome",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Ajouter un tome":
                new_tome = int(inquirer.number(
                    message="Entrez le numéro du tome"
                    " que vous voulez ajouter:").execute())
                try:
                    MangaPhysiqueService().ajouter_tome(
                        manga=L, new_tome=new_tome)

                except Exception as e:
                    print("\n", e)

                return MainMangathequeView(
                    ("\n" + "=" * 50 + " Menu des mangathèques"
                     " :) " + "=" * 50 + "\n")
                )

            case "Enlever un tome":
                tome = int(inquirer.number(
                    message="Entrez le numéro du tome"
                    " que vous voulez supprimer :)").execute())
                try:
                    MangaPhysiqueService().enlever_tome(manga=L, tome=tome)

                except Exception as e:
                    print("\n", e)

                return MainMangathequeView(
                    ("\n" + "=" * 50 + " Menu des mangathèques"
                     " :) " + "=" * 50 + "\n")
                )

            case "Retour":
                return MainMangathequeView(
                    "\n" + "=" * 50 + " Menu des collections"
                    " :) " + "=" * 50 + "\n"
                )
