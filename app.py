import algorithms
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return render_template('index.html', data=None)


@app.route('/jsonreq', methods=['POST'])
def jsonreq(request):
    # Get the JSON data sent from the form
    jsondata = request.form['searchquery']
    print jsondata
    # Convert the JSON data into a Python structure
    return render_template('results.html')


@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    query_string = request.form['search-query']
    results = algorithms.get_patient_data_json(query_string)
    return render_template("results.html", results=results)

if __name__ == '__main__':
    app.run()