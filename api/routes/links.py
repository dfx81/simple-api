import flask
from flask import Blueprint, jsonify

links = Blueprint("links", __name__)

link_list = {
	"hp": "https://dfx-81.web.app",
	"ig": "https://instagram.com/dfx_81",
	"tw": "https://twitter.com/dfx_81",
	"gh": "https://github.com/dfx81",
	"yt": "https://www.youtube.com/channel/UCVc6CZfMGuZZxjRPzZE91Iw"
}

@links.route("/")
def respond():
	res = jsonify(link_list)
	res.headers.add('Access-Control-Allow-Origin', '*')

	return res

@links.route("/<string:tag>")
def redirect(tag):
	res = flask.Response()

	if tag in link_list.keys():
		res.status_code = 301
		res.location = link_list.get(tag)
	else:
		res.status_code = 404
		res.response = "Link not found."
	
	res.access_control_allow_origin = "*"

	return res