from datetime import datetime
from flask import Blueprint, request, jsonify

ping = Blueprint("ping", __name__)

@ping.route("/")
def pong():
    req_time = request.date
    res_time = datetime.now()
    duration = (res_time - req_time).total_seconds()

    res = {
        "message": f"Pong in { round(duration, 2) }s",
        "status": 200
    }

    return jsonify(res)
