import requests

pyynto = "http://api.openweathermap.org/data/2.5/weather?"
api = "dc51723ff3d4c9a75d371d662f47f345"

hakusana = input("Anna kaupunki: ")

kaupunki = pyynto + "appid=" + api + "&q=" + hakusana



try:
    vastaus = requests.get(kaupunki)
    if vastaus.status_code==200:
        vastaus_json = vastaus.json()
        for a in vastaus_json["weather"]:
            print(f"Säätila on: {a['main']}")
        lampo = vastaus_json["main"]["temp"]
        print(f"{int(lampo - 273.15)}°C")
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")