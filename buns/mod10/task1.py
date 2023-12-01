import requests
import json


def load_raw_data(url: str):
    return json.loads(requests.get(url).text)["results"][0]


def filter_data(data: dict, fields: tuple):
    result = dict()

    for key in data.keys():
        if key in fields:
            result[key] = data[key]

    return result


def load_pilots_data(data: dict):
    return [json.loads(requests.get(ref).text) for ref in data["pilots"]]


def correct_pilots_data(pilots: list):
    for i in range(len(pilots)):
        pilots[i] = filter_data(pilots[i], accept_plt_fields)
        home = pilots[i]["homeworld"]
        pilots[i]["homeworld"] = json.loads(requests.get(home).text)["name"]
        pilots[i]["homeworld_url"] = home

    return pilots


if __name__ == "__main__":
    ship_name = "Millennium Falcon"
    accept_ship_fields = ("name", "max_atmosphering_speed", "starship_class", "pilots")
    accept_plt_fields = ("name", "height", "mass", "homeworld")

    raw_data = load_raw_data(f"https://swapi.dev/api/starships/?search={ship_name}")
    raw_data["pilots"] = correct_pilots_data(load_pilots_data(raw_data))

    filtered = json.dumps(filter_data(raw_data, accept_ship_fields), indent=4)

    print(filtered)

    with open("starship.text", mode="w+") as file:
        file.write(filtered)
