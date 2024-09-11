import requests

r = requests.get('https://api.jikan.moe/v4/manga')
r.status_code
print(r.json())

