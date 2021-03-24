from flask import Flask, render_template
from json import loads
import Database


config = loads(open("config.json", 'r').read())
database = Database.connectToDatabase(config)
# markers = Database.getInformationFromDatabase(config, database)  # TODO: marker should show comment information on tap
markers = [list(item[:-1]) for item in Database.getInformationFromDatabase(config, database)]
app = Flask(__name__)


@app.route("/map")
def mapview():
    return render_template('Map/index.html',
                           apikey=config['map api key'],
                           mapCenterLatitude=22.719568,
                           mapCenterLongitude=75.857727,
                           markers=markers)
           

@app.errorhandler(404)
def page_not_found(e):
    return render_template('Error404Page/index.html'), 404


@app.route('/')
def hello_world():
    return render_template('StartPage/index.html', title='welcome')


if __name__ == '__main__':
    app.run(port=80)