from flask import Blueprint, jsonify
import api

listing = Blueprint("listing", __name__)

@listing.route("/<string:id>")
def list_vid_id(id):
	playlist = api.generate_list(api.send_request(f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&playlistId={ id }&key={ api.api_key }"))

	res = {
		"status": 200,
		"lists": [ api.generate_link(vid_id) for vid_id in playlist ]
	}
	
	return jsonify(res)