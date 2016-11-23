import PyISY
import slackbot_settings

class IsyClient:
    def __init__(self, settings):

        self.ADDR = settings.PYISY_ADDR
        self.PORT = settings.PYISY_PORT
        self.USER = settings.PYISY_USER
        self.PASS = settings.PYISY_PASS
        self.login()


    def login(self):
        print( "logging in to ISY...")
        self.client = PyISY.ISY(self.ADDR, self.PORT, self.USER, self.PASS)

    def getStatus(self):
        return self.client.connected

    def setNode(self, nid, on=True):
        if(on):
            self.client.nodes[nid].on()
        else:
            self.client.nodes[nid].off()
        

    

