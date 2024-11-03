import requests

pyynto = "https://api.chucknorris.io/jokes/random"

try:
    vastaus = requests.get(pyynto)
    if vastaus.status_code==200:
        vastaus_json = vastaus.json()
        print(vastaus_json["value"])
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")

