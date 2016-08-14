from flask import Flask, render_template
from magic_num import magic_num, get_standings, get_standings_for_team
from datetime import datetime
from pytz import timezone

app = Flask(__name__)
standings, standings_date = get_standings()
central_time = 'US/Central'
last_updated = datetime.now(timezone(central_time))


@app.route('/<team>')
def index(team):
    global last_updated, central_time, standings_date, standings

    cur_time = datetime.now(timezone(central_time))
    team = team.title()
    if abs(int(cur_time.minute) - int(last_updated.minute)) >= 5:
        standings, standings_date = get_standings()
        last_updated = cur_time

    wildcard, division = get_standings_for_team(standings, team)
    wc_magic_num = magic_num(team, division[team]["won"], wildcard)
    div_magic_num = magic_num(team, division[team]["won"], division)

    if(wc_magic_num <= 0):
        wc_magic_num = "0. The %s have clinched a playoff berth!" % team
    if(div_magic_num <= 0):
        div_magic_num = "0. The %s have clinched the division!" % team
    return render_template("index.html", div_num=div_magic_num, wc_num=wc_magic_num, last_updated=standings_date, team=possessive(team))

def possessive(team):
    if team[-1:] in ['S', 's']:
        return team + '\''
    else:
        return team + '\'s'

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)