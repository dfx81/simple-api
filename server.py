from multiprocessing import Process
import time
from flask import Flask
import sys
import api

# Initialize commandline arguments
if len(sys.argv) <= 5 or not (sys.argv[3].isdigit() and sys.argv[6].isdigit()):
    print("Usage: python server.py [HOST] [ADDRESS] [PORT] [YT-API-KEY] [DEFAULT-PLAYLIST-ID] [UPTIMER]")
    sys.exit(-1)

HOST = sys.argv[1]
IP = sys.argv[2]
PORT = int(sys.argv[3])
UPTIMER = int(sys.argv[6])

api.api_key = sys.argv[4]
api.playlist_id = sys.argv[5]

# Initialize Flask app
app = Flask(__name__)

app.register_blueprint(api.routes.index)
app.register_blueprint(api.routes.links, url_prefix="/links")
app.register_blueprint(api.routes.roulette, url_prefix="/roulette")
app.register_blueprint(api.routes.listing, url_prefix="/list")
app.register_blueprint(api.routes.ping, url_prefix="/ping")

# Setup uptime monitoring job
def monitor(timer):
    while True:
        print(f"Pinging { HOST }")
        res = api.send_request(f"{ HOST }/ping")
        print(f"{ res['status'] }: { res['message'] }")
        
        time.sleep(timer)

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
    uptime_monitor = Process(target=monitor, args=(UPTIMER))
    uptime_monitor.start()