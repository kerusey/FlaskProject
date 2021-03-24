from flask import Flask, render_template
from json import loads


config = loads(open("config.json", 'r').read())
app = Flask(__name__)

@app.route("/map")
def mapview():
    return render_template('Map/index.html',
                           apikey=config['map api key'],
                           latitude=22.719568,
                           longitude=75.857727,
                           address="name of shit")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('Error404Page/index.html'), 404


@app.route('/')
def hello_world():
    return render_template('StartPage/index.html', title='welcome')


if __name__ == '__main__':
    app.run(port=80)