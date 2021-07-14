# import flask library
from flask import Flask

# passing a parameter called name
app = Flask(__name__)

# decorator
# ive started an app
# my default url
# creating a route (home, index, about...)
@app.route('/')
def hello_world():
    return "Hello World"

# adding my second route
@app.route('/index/')
def index():
    return "Welcome to Aaliyah's Homepage"

# adding my 3rd route
@app.route('/index/contact/')
def contact():
    return "Contact me"

# activating my flask app
if __name__ == '__main__':
    app.debug = True
    app.run()
