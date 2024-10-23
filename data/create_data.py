import json
import requests
import time

data = []
erreurs = 0
for i in range(1, 6):
    r = requests.get('https://api.jikan.moe/v4/manga', {"page": i})
    r.status_code
    r = r.json()
    data.append(r)
    print(i)
    time.sleep(1)
    if 'status' in r:
        print("erreur")
        erreurs += 1
        time.sleep(1)


with open("data/data.json", "w") as f:
    json.dump(data, f, indent=4)

print("importation terminé avec tant d'erreur:\n")
print(erreurs)
