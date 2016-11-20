import PyISY
import json

SETTINGS = {}
with open('PyISY.settings.json') as data_file:    
    SETTINGS = json.load(data_file)


isy = PyISY.ISY(SETTINGS['host'], SETTINGS['port'], SETTINGS['username'], SETTINGS['password'])
print(isy.connected)


isy.auto_update = True

node_names = ["ZW002_1"]

def notify(e):
    print('Notification Received')

for nn in node_names:
    node = isy.nodes[nn]
    print nn

    print node.status
    handler = node.status.subscribe('changed', notify)

 
