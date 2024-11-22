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

for i in range(5):
    k = 25
    if (i >= 2903):
        k = 13
    for j in range(k):
        try:
            titre = data[i]["data"][j]["titles"][0]["title"].replace("'", '"')
            titre = titre.encode('utf-8', errors='ignore').decode('utf-8')

            synopsis = data[i]["data"][j]["synopsis"].replace("'", '"')
            synopsis = synopsis.encode('utf-8', errors='ignore').decode('utf-8')
            
            auteurs = ""
            for l in range(len(data[i]["data"][j]["authors"])):
                auteurs += data[i]["data"][j]["authors"][l]["name"]
                if (l != (len(data[i]["data"][j]["authors"]) - 1)):
                    auteurs += ", "
            
            nb_volumes = data[i]["data"][j]["volumes"]
            nb_chapitres = data[i]["data"][j]["chapters"]
            if (nb_volumes == None):
                nb_volumes = "NULL"
            if (nb_chapitres == None):
                nb_chapitres = "NULL"

            res = None

            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO test.manga(titre_manga, synopsis, auteurs, nb_volumes, nb_chapitres)"
                        "VALUES                                              "
                        f"('{titre}', '{synopsis}', '{auteurs}', {nb_volumes}, {nb_chapitres}) "
                        "  RETURNING id_manga;                               ",
                        {
                            "titre_manga": titre,
                            "auteurs": auteurs,
                            "synopsis": synopsis,
                            "nb_volumes": nb_volumes,
                            "nb_chapitres": nb_chapitres
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(titre)
            erreurs += 1
            logging.info(e)
print(f"il y a eu {erreurs} erreurs")
