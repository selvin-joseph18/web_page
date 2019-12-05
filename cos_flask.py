from flask import Flask, render_template, request
from src.driver.scientific_calc import ScientificCalc

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/calculate")
def calculate():
    return render_template('calculate.html')

@app.route("/response",methods=['POST'])
def response():
    if request.method == 'POST':
        angle = request.form['angle']
        c1 = ScientificCalc()
        result = c1.calculate_cos(angle)
    return render_template('response.html',value=result)

if __name__=='__main__':
    app.run(debug=True)
