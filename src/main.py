import requests
for i in range(1, 2000):
    r = requests.get('https://api.jikan.moe/v4/manga', {"page" :1})
    r.status_code
    print(r.json())

