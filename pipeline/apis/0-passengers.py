import requests


def availableShips(passengerCount):
    ships = []
    url = "https://swapi.dev/api/starships/"

    while url:
        response = requests.get(url)
        data = response.json()
        for ship in data['results']:
            passengers = ship['passengers'].replace(',', '')
            if passengers.isdigit() and int(passengers) >= passengerCount:
                ships.append(ship['name'])
        url = data['next']

    return ships
