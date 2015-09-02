import requests

def magic_num():
    url = "https://erikberg.com/mlb/standings.json"

    response = requests.get(url).json()

    for team in response["standing"]:
        if team["last_name"] == "Cubs":
            cubs = team
        if team["last_name"] == "Giants":
            giants = team

    if cubs and giants:
        magic_num = 163 - int(cubs["won"]) - int(giants["lost"])

    return (magic_num)
