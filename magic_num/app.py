from flask import Flask, render_template
from magic_num import magic_num, get_standings
from datetime import datetime
from pytz import timezone

app = Flask(__name__)
wildcard, division, standings_date = get_standings("Cubs")
central_time = 'US/Central'
last_updated = datetime.now(timezone(central_time))


@app.route('/')
def index():
    global wildcard, division, last_updated, central_time, standings_date

    cur_time = datetime.now(timezone(central_time))
    if abs(int(cur_time.minute) - int(last_updated.minute)) >= 5:
        wildcard, division, standings_date = get_standings("Cubs")
        last_updated = cur_time

    wc_magic_num = magic_num("Cubs", division["Cubs"]["won"], wildcard)
    div_magic_num = magic_num("Cubs", division["Cubs"]["won"], division)

    magic_number = min(wc_magic_num, div_magic_num)
    if(magic_number <= 0):
        magic_number = "0. The Cubs have clinched a playoff berth!"
    return render_template("index.html", num=magic_number, last_updated=standings_date)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)