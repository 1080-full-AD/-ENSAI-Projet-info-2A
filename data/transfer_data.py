import json
import logging

from src.utils.singleton import Singleton
from src.utils.singleton import Singleton
from src.utils.log_decorator import log

from src.dao.db_connection import DBConnection

from src.business_objet.manga import Manga

with open('data/data.json', 'r') as f:
    data = json.load(f)

erreurs = 0

for i in range(2904):
    k = 25
    if (i >= 2903):
        k = 13
    for j in range(k):
        try:
            id_manga = data[i]["data"][j]["mal_id"]
            print(id_manga)
            titre = data[i]["data"][j]["title_english"].replace("'", '"')
            titre = titre.encode('utf-8', errors='ignore').decode('utf-8')
            print(titre)
            synopsis = data[i]["data"][j]["synopsis"].replace("'", '"')
            synopsis = synopsis.encode('utf-8', errors='ignore').decode('utf-8')
            auteurs = ""
            for l in range(len(data[i]["data"][j]["authors"])):
                auteurs += data[i]["data"][j]["authors"][l]["name"]
                if (l != (len(data[i]["data"][j]["authors"]) - 1)):
                    auteurs += ", "
            print(auteurs)

            res = None

            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet.manga(id_manga, titre_manga, synopsis, auteurs)"
                        "VALUES                                              "
                        f"({id_manga}, '{titre}', '{synopsis}', '{auteurs}') "
                        "  RETURNING id_manga;                               ",
                        {
                            "id_manga": id_manga,
                            "titre_manga": titre,
                            "auteurs": auteurs,
                            "synopsis": synopsis
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            erreurs += 1
            logging.info(e)
print(f"il y a eu {erreurs} erreurs")

