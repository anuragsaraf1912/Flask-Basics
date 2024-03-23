from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "example"

"""
There are 4 major ways to transfer data around: 
1. GET request 
2. POST form request
3. Adding to the URL as done in 'results' route
4. Saving the data in session and using it for different purpose

"""

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/results/<float:score>')
def result(score):
    return render_template('results.html', score = score, details = session, resultURL = url_for('details'))

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        finance = float(request.form['Finance'])
        stats = float(request.form['Statistics'])
        compSc = float(request.form['CompScience'])
        total_score = (finance+stats+compSc)/3
        session['Finance'] = finance
        session['Statistics'] = stats
        session['Computer Science'] = compSc

    return redirect(url_for('result', score=round(total_score,2)))

@app.route('/details')
def details():
    return render_template('details.html', data=session)

if __name__ == '__main__':
    app.run(debug = True)