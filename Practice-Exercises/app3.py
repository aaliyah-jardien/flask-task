from flask import Flask, render_template

# simple html template
app = Flask(__name__)

@app.route('/<name>', methods=['GET', 'POST'])
def home(name):
    return render_template('homepage.html', name=name)

@app.route('/looping/<int:number>')
def looping(number):
    return render_template('loopy.html', number=number)

@app.route('/image', methods=['GET', 'POST'])
def image():
    return render_template('image.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
