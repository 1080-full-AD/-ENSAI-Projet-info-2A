from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.manga_service import MangaService
from src.business_objet.manga_physique import MangaPhysique
from src.service.manga_physique_service import MangaPhysiqueService
from src.views.session import Session
from src.views.users.main_mangatheque_view import MainMangathequeView


class CreateMangathequeView(AbstractView):
    """Menu principal des avis"""

    def choisir_menu(self):
        """Choix du menu suivant

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        try:
            user = Session().getuser()
            id_utilisateur = user.id_utilisateur

            titre = inquirer.text("Entrez le nom du manga :)").execute()
            manga = MangaService().rechercher_un_manga(titre)
        except Exception as e:
            print("\n", e)
            return MainMangathequeView(
                "\n" + "=" * 50 + " Menu des" " Mangathèques :) " + "=" * 50 + "\n"
            )
        missing = inquirer.confirm(message="Vous manque-t-il des tomes ? ").execute()
        try:
            if missing is True:
                tomes_manquants = inquirer.text(
                    message="Entrez les tomes manquants séparés par des virgules (ex: 1, 3, 7):"
                ).execute()
                tomes_manquants = [x.strip() for x in tomes_manquants.split(",")]
                tomes_manquants = [int(x) for x in tomes_manquants]
            else:
                tomes_manquants = None
        except Exception as e:
            print("\n", e)
            return MainMangathequeView(
                "\n" + "=" * 50 + " Menu des" " Mangathèques :) " + "=" * 50 + "\n"
            )
        try:
            status = inquirer.select(
                message="Le manga est-t-il toujours en cours ou terminé ? ",
                choices=["En cours", "Terminé"],
            ).execute()
            dernier_tome = int(
                inquirer.number(
                    message="Quel est le numéro du dernier tome que vous possédez ?"
                ).execute()
            )
            mangatheque = MangaPhysique(
                id_manga=manga.id_manga,
                id_utilisateur=id_utilisateur,
                titre_manga=manga.titre_manga,
                auteurs=manga.auteurs,
                synopsis=manga.synopsis,
                nb_chapitres=manga.nb_chapitres,
                nb_volumes=manga.nb_volumes,
                tomes_manquants=tomes_manquants,
                dernier_tome=dernier_tome,
                status=status,
            )
            MangaPhysiqueService().creer_manga_physique(manga=mangatheque)

        except Exception as e:
            print("\n", e)

        return MainMangathequeView(
            "\n" + "=" * 50 + " Menu des" " Mangathèques :) " + "=" * 50 + "\n"
        )
