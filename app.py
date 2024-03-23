
#THIS IS THE BASIC VERSION OF THE FLASK APP
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1>This is my Server</h1>"

@app.route('/success/<int:score>')
def success(score):
    return "<h1>Passed with Score "+ str(score) + "</h1>"

@app.route('/fail/<int:score>')
def fail(score):
    return "<h1>Failed with Score "+ str(score) + "</h1>"

@app.route('/results/<int:score>')
def result(score):
    if score < 50: return redirect(url_for('fail', score = score))
    else: return redirect(url_for('success', score = score))

if __name__ == '__main__':
    app.run(debug = True)