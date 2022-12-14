import flask
from flask import Blueprint
import api

roulette = Blueprint("roulette", __name__)

@roulette.route("/")
def redirect():
	res = flask.Response()

	res.access_control_allow_origin = "*"
	res.status_code = 302
	link = api.get_random_vid(api.vid_list)
	res.location = link
	
	return res

@roulette.route("/<string:id>")
def custom_redirect(id):
	playlist = api.get_vid_list(id)

	res = flask.Response()

	res.access_control_allow_origin = "*"
	res.status_code = 302
	link = api.get_random_vid(playlist)
	res.location = link
	
	return res