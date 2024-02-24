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



@app_views.route('/polling_unit_result', methods=['GET'], strict_slashes=False)
def polling_unit_result():
    """
    list all polling result
    """

    all_Agentname = storage.all(Agentname).values()
    all_Announced_ward_results = storage.all(Announced_ward_results).values()
    all_Lga = storage.all(Lga).values()
    all_Party = storage.all(Party).values()
    all_Polling_unit = storage.all(Polling_unit).values()
    all_States = storage.all(States).values()
    all_Ward = storage.all(Ward).values()
    all_Announced_lga_results = storage.all(Announced_lga_results).values()
    all_Announced_pu_results = storage.all(Announced_pu_results).values()
    all_Announced_state_results = storage.all(Announced_state_results).values()

    state_name = request.get("state_id")
    if not state_id or state_id == 25:
        return
    polling_unit_uniq_id = str(request.get("uniqueid"))
    if not polling_unit_uniq_id:
        return

    req_poll_res = []
    for p in all_Announced_pu_results:
    	if p.polling_unit_uniqueid == polling_unit_uniq_id:
            req_poll_res.append(p)
    if len(req_poll_res) == 0:
        return
    all_Party_dict = {}
    for b in all_Party:
        all_Party_dict[b.id] = b.partyid
    res = {}
    for f in all_Party_dict.values():
        res[f] = 0
    for c in req_poll_res:
        for g in all_Party_dict.values():
            if g == c.party_abbreviation:
                res[g] = res[g] + c.party_score
    return jsonify(res)


@app_views.route('/lga_announced_result', methods=['GET'], strict_slashes=False)
def lga_result():
    """
    list all lga result
    """

    all_Agentname = storage.all(Agentname).values()
    all_Announced_ward_results = storage.all(Announced_ward_results).values()
    all_Lga = storage.all(Lga).values()
    all_Party = storage.all(Party).values()
    all_Polling_unit = storage.all(Polling_unit).values()
    all_States = storage.all(States).values()
    all_Ward = storage.all(Ward).values()
    all_Announced_lga_results = storage.all(Announced_lga_results).values()
    all_Announced_pu_results = storage.all(Announced_pu_results).values()
    all_Announced_state_results = storage.all(Announced_state_results).values()


    lga_ids = []
    for k in all_Lga:
        lga_ids.append(k.lga_id)
    lga_polling_units = {}
    for l in lga_ids:
        lga_polling_units[l] = []
    for m in all_Polling_unit:
        for n in lga_polling_units.keys():
            if m.lga_id == n:
                lga_polling_units[n].append(m.uniqueid)

    state_name = request.get("state_id")
    if not state_id or state_id == 25:
        return

    lga_results = {}
    for r in lga_ids:
        lga_results[r] = {}
        for b in all_Party:
            lga_results[r][b.partyid] = 0

    for lgas, poll_units in lga_polling_units.items():
        for poll_unit in poll_units:
            for each_res in all_Announced_pu_results:
    	        if each_res.polling_unit_uniqueid == str(poll_unit):
                    lga_results[lgas][each_res.party_abbreviation] += party_score

    return jsonify(lga_results)
