from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.manga_service import MangaService
from src.views.session import Session
from src.views.users.main_mangatheque_view import MainMangathequeView


class CreateCollectionView(AbstractView):
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

            titre = inquirer.text(
                "Entrez le nom du manga :)"
            ).execute()
            manga = MangaService().rechercher_un_manga(titre)
            mangatheque = MangaPhysique(id_manga=manga.id_manga, id_utilisateur=id_utilisateur, titre_manga=manga.titre_manga, auteurs=manga.auteurs, synopsis=manga.synopsisn tomes_manquant)

        except Exception as e:
            print("\n", e)
            return MainMangathequeView("\n" + "=" * 50 + " Menu des"
                                        " Mangathèques :) " + "=" * 50 + "\n")

        description = inquirer.text(
            "Entrez une description pour votre collection :)"
        ).execute()

        CollectionVirtuelleService().modifier_description(collection=collection, new_description=description)
        ajout = True

        while ajout is True:
            titre_manga = inquirer.text(
                f"Entrez le nom du manga que vous voulez ajouter à {titre} :)"
            ).execute()
            try:
                manga = MangaService().rechercher_un_manga(
                    titre_manga=titre_manga
                    )
                CollectionVirtuelleService().ajouter_manga(collection=collection, new_manga=manga)
            except Exception as e:
                print("\n", e, "\n")
            ajout = inquirer.confirm("Voulez-vous ajouter un autre manga?").execute()
        print(f'\n La collection {titre} a été créée avec succès :)')

        return MainCollectionView("\n" + "=" * 50 + " Menu des"
                                        " collections " + "=" * 50 + "\n")
