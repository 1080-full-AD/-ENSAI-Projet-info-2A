
import logging
import dotenv


from src.views.accueil.main_menu_view import MainView


if __name__ == "__main__":

    dotenv.load_dotenv(override=True)

    vue_courante = MainView("\n" + "=" * 50 + " Bienvenue"
                            " :) " + "=" * 50 + "\n")

    while vue_courante:
        try:
            vue_courante.afficher()
            vue_courante = vue_courante.choisir_menu()
        except Exception as e:
            logging.info(e)
            vue_courante = MainView(e)
