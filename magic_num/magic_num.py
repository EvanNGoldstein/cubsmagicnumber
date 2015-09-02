import requests

def magic_num():
    url = "https://erikberg.com/mlb/standings.json"
    headers = {
        "User-agent": "cubsmagicnumber/0.0.0 (eng2112@columbia.edu)"
    }

    teams = {}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response = response.json()
    else:
        return response.reason


    for team in response["standing"]:
        teams[team["last_name"]] = (team["won"], team["lost"])
        # if team["last_name"] == "Cubs":
        #     cubs = team
        # if team["last_name"] == "Giants":
        #     giants = team

    cubs = teams["Cubs"]
    giants = teams["Giants"]
    nationals = teams["Nationals"]
    if cubs and giants:
        magic_num_giants = 163 - int(cubs[0]) - int(giants[1])
        magic_num_nationals = 163 - int(cubs[0]) - int(nationals[1])
    if magic_num_giants >= magic_num_nationals:
        magic_num = magic_num_giants
    else:
        magic_num = magic_num_nationals

    return (magic_num, response["standings_date"])

