from flask import Flask
from initialize import init
import argparse
from gevent import pywsgi

# Entrance of the application
app = Flask(__name__)

# parse user argument
parser = argparse.ArgumentParser()
# basic arguments
parser.add_argument('--host', type=str, help='The IP address of server', default="localhost")
parser.add_argument('--port', type=int, help='The port of the service', default=8000)
parser.add_argument('--download', help='To download the reqired models', action='store_true', default=False)
# args for detector
parser.add_argument('--device', type=int, help='The device of test detector (-1 for cpu | 0,1,2,3 for gpu ids)', default='-1')
args = parser.parse_args()

if __name__ == '__main__':
    print("--Starting Server--")
    init(app, args)  # initialize the application

    server = pywsgi.WSGIServer((args.host, args.port), app)
    server.serve_forever()
