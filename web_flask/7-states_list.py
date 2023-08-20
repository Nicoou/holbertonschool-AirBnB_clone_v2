#!/usr/bin/python3
""" task 7 """
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


app.teardown_appcontext


def teardown_db(exeption):
    """remove the current SQLAlchemy"""
    storage.close


@app.route("/states_list", strict_slashes=False)
def states_list():
    """render states"""
    return render_template("7-states_list.html",
                           states=storage.all("State").values())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
