import json
from src.dao.manga_dao import *
from src.Business_objet.manga import *

with open('data/data.json', 'r') as f:
    data = json.load(f)

for i in range(1, 2):
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
        for e in data[i]["data"][j]["authors"]:
            auteurs += e["name"]
            auteurs += ", "
        print(auteurs)
        manga_actuel = Manga(
            id_manga,
            titre,
            synopsis,
            auteurs
        )
        mangadao = MangaDao()
        print(mangadao.creer_manga(manga_actuel))
