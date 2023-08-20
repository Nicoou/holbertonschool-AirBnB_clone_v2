#!/usr/bin/python3
""" task 7 """
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """remove the current SQLAlchemy"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """render states"""
    return render_template('8-cities_by_states.html',
                           states=storage.all("State").values())


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
