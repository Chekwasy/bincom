#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from models.agentname import Agentname
from models.announced_ward_results import Announced_ward_results
from models.lga import Lga
from models.party import Party
from models.polling_unit import Polling_unit
from models.states import States
from models.ward import Ward
from models.base_model import BaseModel, Base
from models.announced_lga_results import Announced_lga_results
from models.announced_pu_results import Announced_pu_results
from models.announced_state_results import Announced_state_results
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request



@app_views.route('/chekwasy_farm/2626632/all_order', methods=['GET'], strict_slashes=False)
def list_farm_user():
    """
    list all farm user
    """

    lst = []
    all_fm = storage.all(Farm).values()

    for dic in all_fm:
    	lst.append(dic.to_dict())
    return jsonify(lst)


