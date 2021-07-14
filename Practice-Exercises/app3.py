from flask import Flask, render_template

# simple html template
app = Flask(__name__)

@app.route('/<name>')
def home(name):
    return render_template('homepage.html', name=name)

@app.route('/looping/<int:number>')
def looping(numbers)
    return render_template('loopy.html', number=number)

if __name__ == '__main__':
    app.debug = True
    app.run()