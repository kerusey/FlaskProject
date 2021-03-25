from flask import Flask, render_template
from json import loads
import Database


config = loads(open("config.json", 'r').read())
app = Flask(__name__)


@app.route("/3dmap")
def map3DView():
    return render_template('3DMap/index.html',
                           apikey=config['3DMap api key'])


@app.route("/map")
def mapview():
    database = Database.connectToDatabase(config)
    markersInformation = Database.getInformationFromDatabase(config, database)
    markersCoordinates = [list(item[:-1]) for item in markersInformation]
    markersComments = [list(item[-1]) for item in markersInformation]
    return render_template('Map/index.html',
                           apikey=config['map api key'],
                           mapCenterLatitude=22.719568,
                           mapCenterLongitude=75.857727,
                           markers=markersCoordinates,
                           markerComments=markersComments)
           

@app.errorhandler(404)
def page_not_found(e):
    return render_template('Error404Page/index.html'), 404


@app.route('/')
def hello_world():
    return render_template('StartPage/index.html', title='welcome')


if __name__ == '__main__':
    app.run(port=80)