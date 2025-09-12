import requests

ANIMAL = "fox"
url = f"https://api.api-ninjas.com/v1/animals?name={ANIMAL}"
params = {"X-Api-Key": "sqxq+uQNGhWNlbY7oYFbmg==hYHrc0liP2QMeFKH"}

response = requests.get(url, params=params)
if response.status_code == 200 and response.json() != []:
    data = response.json()
else:
    print("Response code:", response.status_code)
    print(f"Animal {ANIMAL} NOT found")
