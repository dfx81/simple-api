import requests
import random
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
    print(api.api_key)
    res = requests.get(url)

    if res != None:
        return res.json()

def get_vid_list(id):
    return generate_list(send_request(f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&playlistId={ id }&key={ api.api_key }"))

def get_random_vid(playlist):
    return generate_link(playlist[random.randint(0, len(playlist) - 1)])

vid_list = []