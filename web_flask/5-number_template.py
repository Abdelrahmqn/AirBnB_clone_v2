#!/usr/bin/python3
""" Flask Documentation file """


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def its_hbnb():
    return 'HBNB'


@app.route('/c/<element>', strict_slashes=False)
def print_text(element):
    return f"C %s" % element


@app.route('/python/', strict_slashes=False)
def print_cool():
    return "Python is cool"


@app.route('/python/<input>', strict_slashes=False)
def print_argument(input):
    formatted = input.replace("_", " ")
    return f"Python %s" % formatted


@app.route('/number/<int:number>', strict_slashes=False)
def number_n(number):
    return "%i is a number" % number


@app.route('/number_template/<int:numb>', strict_slashes=False)
def number_template(numb):
    return render_template('5-number.html', numb=numb)


if __name__ == '__main__':
    app.run(port=5000, debug=True, host="0.0.0.0")
