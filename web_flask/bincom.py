#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.agentname import Agentname
from models.announced_ward_results import Announced_ward_results
from models.lga import Lga
from models.party import Party
from models.polling_unit import Polling_unit
from models.states import States
from models.ward import Ward
from models.announced_lga_results import Announced_lga_results
from models.announced_pu_results import Announced_pu_results
from models.announced_state_results import Announced_state_results
from os import environ
from flask import Flask, render_template
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/', strict_slashes=False)
def chekwasy():
    """ Chekwasy is alive! """

    return render_template('bincom.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
