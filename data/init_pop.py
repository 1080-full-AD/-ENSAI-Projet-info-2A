import json

with open("data/data.json", "r") as f:
    data = json.load(f)

pop = "INSERT INTO projet.manga (id_manga,titre_manga,synopsis,auteurs,nb_volumes,nb_chapitres) VALUES \n"

last_page = 1

for i in range(0, last_page):
    k = 25
    if i >= 2903:
        k = 13
    for j in range(k):
        id_manga = data[i]["data"][j]["mal_id"]
        titre = data[i]["data"][j]["titles"][0]["title"].replace("'", '"')
        synopsis = (data[i]["data"][j]["synopsis"]).replace("'", '"')
        auteurs = ""
        for l in range(len(data[i]["data"][j]["authors"])):
            auteurs += data[i]["data"][j]["authors"][l]["name"]
            if l != (len(data[i]["data"][j]["authors"]) - 1):
                auteurs += ", "
        nb_volumes = data[i]["data"][j]["volumes"]
        nb_chapitres = data[i]["data"][j]["chapters"]
        if nb_volumes == None:
            nb_volumes = "NULL"
        if nb_chapitres == None:
            nb_chapitres = "NULL"
        info = f"({id_manga}, '{titre}', '{synopsis}', '{auteurs}',{nb_volumes},{nb_chapitres})"
        print(info)
        pop += info
        if i == last_page - 1 and j == k - 1:
            pop += ";"
        else:
            pop += ",\n"


with open("data/pop_db.sql", "w") as file:
    file.write(pop)
