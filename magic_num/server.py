from flask import Flask, render_template
from magic_num import magic_num
from datetime import datetime
from pytz import timezone

app = Flask(__name__)
cur_magic_num, standings_date = magic_num()
central_time = 'US/Central'
last_updated = datetime.now(timezone(central_time))


@app.route('/')
def index():
    global last_updated
    global cur_magic_num
    global central_time
    global standings_date

    cur_time = datetime.now(timezone(central_time))
    if abs(int(cur_time.minute) - int(last_updated.minute)) >= 5:
        cur_magic_num, standings_date = magic_num()
        last_updated = cur_time

    return render_template("index.html", num=cur_magic_num, last_updated=standings_date)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)