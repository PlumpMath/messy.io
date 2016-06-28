#!/usr/bin/python
import PyISY
import json
from flask import Flask
app = Flask(__name__, static_folder='static', static_url_path='')

def isy_setup():
    global isy
    SETTINGS = {}
    with open('settings/PyISY.settings.json') as data_file:    
        SETTINGS = json.load(data_file)

    isy = PyISY.ISY(SETTINGS['host'], SETTINGS['port'], SETTINGS['username'], SETTINGS['password'])
    print(isy.connected)

    isy.auto_update = True
    return isy

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route("/rest/status/")
@app.route("/rest/status/<node_name>")
def get_node_status(node_name=None):
    try:
        node = isy.nodes[node_name]
        print node.status
        return str(node.status)
    except Exception:
        return "No such node!"

if __name__ == "__main__":
    isy_setup()
    app.run(host='0.0.0.0', port=5002)

