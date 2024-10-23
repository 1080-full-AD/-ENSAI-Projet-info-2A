import json
import logging

from src.utils.singleton import Singleton
from src.utils.singleton import Singleton
from src.utils.log_decorator import log

from src.dao.db_connection import DBConnection

from src.Business_objet.manga import Manga

with open('data/data.json', 'r') as f:
    data = json.load(f)

for i in range(0, 1):
    k = 25
    if (i >= 2903):
        k = 13
    for j in range(k):
        id_manga = data[i]["data"][j]["mal_id"]
        print(id_manga)
        titre = data[i]["data"][j]["title_english"]
        print(titre)
        synopsis = data[i]["data"][j]["synopsis"]
#print(synopsis)
        auteurs = ""
        for l in range(len(data[i]["data"][j]["authors"])):
            auteurs += data[i]["data"][j]["authors"][l]["name"]
            if (l != (len(data[i]["data"][j]["authors"]) - 1)):
                auteurs += ", "
        print(auteurs)

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet.manga(id_manga, titre_manga, synopsis, auteurs)"
                        "VALUES                                              "
                        "(%(id_manga)s, %(titre)s, %(auteurs)s, %(synopsis)s) "
                        "  RETURNING id_manga;                               ",
                        {
                            "id_manga": id_manga,
                            "titre": titre,
                            "auteurs": auteurs,
                            "synopsis": synopsis
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        print(res)
        if res:
            print(res["id_manga"])
            created = True

        print(created)
