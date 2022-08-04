import flask
from flask import Blueprint

index = Blueprint("index", __name__)

@index.route("/")
def help():
	message = (
		"<h1>Simple API created by dfx</h1>"
		"<h2>Endpoints</h2>"
		"<ul>"
		"<li><b>[GET]</b> <code>/</code> : View this page</li>"
		"<li><b>[GET]</b> <code>/ping</code> : Ping the API</li>"
		"<li><b>[GET]</b> <code>/link</code> : Get list of links to dfx's socials</li>"
		"<li><b>[GET]</b> <code>/roulette</code> : Get a random Vocaloid/UTAU song curated by dfx</li>"
		"<li><b>[GET]</b> <code>/roulette/&lt;playlist-id&gt;</code> : Create your own roulette</li>"
		"<li><b>[GET]</b> <code>/list/&lt;playlist-id&gt;</code> : Get list of items in playlist</li>"
		"</ul>"
		"<small>&copy; 2022, QLYCO / dfx</small>"
	)

	res = flask.Response(message)
	
	return res
