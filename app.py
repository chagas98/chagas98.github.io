from flask import Flask, render_template
from random_cap import show_cap

app = Flask(__name__)

@app.route('/')
def script_output():
    variable = show_cap()
    return render_template('index.html',variable= variable)

if __name__ == "__main__":
    app.run(debug = True)