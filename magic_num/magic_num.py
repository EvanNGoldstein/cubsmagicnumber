import requests

def get_standings():
    url = "https://erikberg.com/mlb/standings.json"
    headers = {
        "User-Agent": "cubsmagicnumber/0.0.0 (eng2112@columbia.edu)"
    }

    standings = {}

    response = requests.get(url, headers=headers).json()

    for team in response["standing"]:
        standings[team["last_name"]] = team

    return (standings, response["standings_date"])

def get_standings_for_team(standings, team_name):
    league = standings[team_name]["conference"]
    division_name = standings[team_name]["division"]


    wins = standings[team_name]["won"]

    max_wc_win = 0.0
    top_wc_team = ""

    wildcard = {}
    division = {}

    for team in standings:
        if standings[team]["conference"] == league and standings[team]["rank"] != 1:
            wildcard[team] = standings[team]
            if standings[team]["win_percentage"] > max_wc_win:
                max_wc_win = standings[team]["win_percentage"]
                top_wc_team = team

        if standings[team]["conference"] == league and standings[team]["division"] == division_name:
            division[team] = standings[team]

    wildcard = {team:wildcard[team] for team in wildcard if team != top_wc_team} #TODO: consider moving this logic out of this function

    return (wildcard, division)

def magic_num(team_name, team_wins, standings):
    magic_num = 0

    for team in standings:
        if team != team_name:
            elim_num = 163 - team_wins - standings[team]["lost"]
            if(elim_num > magic_num):
                magic_num = elim_num

    return magic_num

