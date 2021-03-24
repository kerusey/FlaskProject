from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('Error404Page/index.html'), 404


@app.route('/')
def hello_world():
    return render_template('StartPage/index.html', title='welcome')


if __name__ == '__main__':
    app.run(port=80)