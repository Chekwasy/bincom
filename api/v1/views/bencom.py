#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from models.bencom import Bencom
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


