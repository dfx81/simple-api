import random
import flask
from flask import Blueprint
import api

roulette = Blueprint("roulette", __name__)

@roulette.route("/")
def redirect(tag):
	res = flask.Response()

	res.status_code = 301
	res.location = api.generate_link(random.randint(0, len(api.vid_list)))
	
	return res

@roulette.route("/<string:id>")
def custom_redirect(id):
	playlist = api.generate_list(api.send_request(f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&playlistId={ id }&key={ api.api_key }"))

	res = flask.Response()

	res.status_code = 301
	res.location = api.generate_link(random.randint(0, len(playlist)))
	
	return res