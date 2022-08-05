from datetime import datetime
from flask import Blueprint, request, jsonify

ping = Blueprint("ping", __name__)

@ping.route("/")
def pong():
    res = {
        "message": f"Pong! API is running.",
        "status": 200
    }

    res = jsonify(res)
    res.headers.add('Access-Control-Allow-Origin', '*')
	
    return res
