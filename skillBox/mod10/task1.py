import requests
import json


url_star_ship = "https://swapi.dev/api/starships"
url_people = "https://swapi.dev/api/people"


def millennium_falcon(starship_url):
    starship_info = {}
    response_starship = requests.get(starship_url + "/10").json()

    starship_pilots = response_starship["pilots"]
    pilots_info = []
    for i in range(len(starship_pilots)):
        pilot_info = {}
        pilot_response = requests.get(starship_pilots[i]).json()
        pilot_info["name"] = pilot_response["name"]
        pilot_info["height"] = pilot_response["height"]
        pilot_info["mass"] = pilot_response["mass"]
        pilot_info["homeworld"] = requests.get(pilot_response["homeworld"]).json()["name"]
        pilot_info["homeworld_url"] = pilot_response["homeworld"]
        pilots_info.append(pilot_info)

    starship_info["starship_name"] = response_starship["name"]
    starship_info["max_atmosphering_speed"] = response_starship["max_atmosphering_speed"]
    starship_info["starship_class"] = response_starship["starship_class"]
    starship_info["pilots"] = pilots_info

    return starship_info


def create_json_file():
    with open('../data.json', 'w') as file:
        json.dump(millennium_falcon(url_star_ship), file, indent=4)


print(millennium_falcon(url_star_ship))
