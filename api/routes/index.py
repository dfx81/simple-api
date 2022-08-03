import flask
from flask import Blueprint

index = Blueprint("index", __name__)

@index.route("/")
def help():
	message = (
		"# Simple API created by dfx\n"
		"\n  "
		"## Endpoints\n"
		"- [GET] / : View this page  \n"
		"- [GET] /ping : Ping the API  \n"
		"- [GET] /link : Get list of links to dfx's socials  \n"
		"- [GET] /roulette : Get a random Vocaloid/UTAU song curated by dfx  \n"
		"- [GET] /roulette/<playlist-id> : Create your own roulette  \n"
		"- [GET] /list/roulette/<playlist-id> : Get list of items in playlist  \n"
		"\n  "
		"\n(C) 2022, QLYCO / dfx"
	)

	res = flask.Response(message)
