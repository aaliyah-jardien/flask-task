from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<name>')
def home(name):
    return render_template('home_page.html', name=name)


if __name__ = '__main__':
    app.debug = True
    app.run()
