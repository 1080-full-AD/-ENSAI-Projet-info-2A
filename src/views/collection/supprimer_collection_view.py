from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.collection_service import CollectionVirtuelleService
from src.views.session import Session
from src.views.users.main_collection_view import MainCollectionView


class SupprimerCollectionView(AbstractView):
    """Menu principal des avis"""

    def choisir_menu(self):
        """Choix du menu suivant

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        titre = inquirer.text(
            message="Donnez le titre de la collection"
            " que vous souhaitez supprimer :)",
        ).execute()

        user = Session().getuser()
        id_utilisateur = user.id_utilisateur

        try:
            collection = CollectionVirtuelleService().rechercher_collection(
                id_utilisateur=id_utilisateur, titre_collec=titre
            )
            CollectionVirtuelleService().supprimer(collection)

        except Exception as e:
            print("\n", e)

        return MainCollectionView(
            "\n" + "=" * 50 + " Menu des collection" " :) " + "=" * 50 + "\n"
        )
