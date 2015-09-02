from flask import Flask, render_template
from magic_num import magic_num

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", num=magic_num())

if __name__ == '__main__':
    app.run(host="0.0.0.0")