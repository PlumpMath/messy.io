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
        self.isy = PyISY.ISY(self.ADDR, self.PORT, self.USER, self.PASS)

    def getStatus(self):
        return self.isy.connected

    def setNode(self, nid, on=True):
        if(on):
            self.isy.nodes[nid].on()
        else:
            self.isy.nodes[nid].off()
        

    

