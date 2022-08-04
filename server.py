from multiprocessing import Process
import time
from flask import Flask
from waitress import serve
import sys
import api
import api.routes

# Initialize commandline arguments
if len(sys.argv) < 7 or not (sys.argv[3].isdigit() and sys.argv[6].isdigit()):
    print("Usage: python server.py [HOST] [ADDRESS] [PORT] [YT-API-KEY] [DEFAULT-PLAYLIST-ID] [UPTIMER]")
    sys.exit(-1)

HOST = sys.argv[1]
IP = sys.argv[2]
PORT = int(sys.argv[3])
UPTIMER = int(sys.argv[6])

api.api_key = sys.argv[4]
api.playlist_id = sys.argv[5]
api.vid_list = api.get_vid_list(api.playlist_id)

# Initialize Flask app
app = Flask(__name__)

app.register_blueprint(api.routes.index, url_prefix="/api")
app.register_blueprint(api.routes.links, url_prefix="/api/links")
app.register_blueprint(api.routes.roulette, url_prefix="/api/roulette")
app.register_blueprint(api.routes.listing, url_prefix="/api/list")
app.register_blueprint(api.routes.ping, url_prefix="/api/ping/")

# Setup uptime monitoring job
def monitor(timer):
    while True:
        print(f"Pinging in { timer }s.")
        time.sleep(timer)
        print(f"Pinging { HOST }")
        res = api.send_request(f"{ HOST }/ping/")
        if res:
            print(f"{ res['status'] }: { res['message'] }")
        else:
            print("API is down.")

if __name__ == "__main__":
    uptime_monitor = Process(target=monitor, args=(UPTIMER, ))
    print("Starting monitoring process...")
    uptime_monitor.start()
    print("Starting web process...")
    # app.run(host=IP, port=PORT)
    serve(app, host=IP, port=PORT)