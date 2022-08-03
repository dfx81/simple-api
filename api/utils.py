import requests
import api

def generate_list(body):
    if body == None:
        return []
    
    vid_list = [ vid["contentDetails"]["videoId"] for vid in body["items"] ]
    return vid_list

def generate_link(id):
    link = f"https://youtu.be/{ id }"
    return link

def send_request(url):
    res = requests.get(url)

    if res.status_code == 200:
        return res.json()
    else:
        return None

vid_list = generate_list(send_request(f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&playlistId={ api.playlist_id }&key={ api.api_key }"))