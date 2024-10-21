import json
import requests
import time

for i in range(1, 6):
    with open("data/data.json", "w") as f:
        r = requests.get('https://api.jikan.moe/v4/manga', {"page": i})
        r.status_code
        r = r.json()
        print(i)
        json.dump(r, f)
        time.sleep(0.34)
