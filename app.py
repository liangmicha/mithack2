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
    # if query_string == "Arjun Dubar xrays before April":
    # return render_template('results_xrays.html', results=algorithms.get_patient_data_json(query_string))
    # if query_string == "Sanjit before March 2015 prescriptions":
    return render_template('results_prescription.html', results=algorithms.get_patient_data_json(query_string))
    # if query_string == "Arjun Dubar notes":
    #     return render_template('results_notes.html', results=algorithms.get_patient_data_json(query_string))
    # if query_string == "Kumar m. lab tests":
    #     return render_template('results_tests.html', results=algorithms.get_patient_data_json(query_string))

@app.route('/xray_viewer')
def image_viewer():
    return render_template('../image_viewer/viewers/index.html')

if __name__ == '__main__':
    app.run()