import PyISY

class IsyClient:
    def __init__(self):

        f = open('plugins/PyISY.settings.txt', 'r')
        self.ADDR = f.readline().strip()
        self.PORT = f.readline().strip()
        self.USER = f.readline().strip()
        self.PASS = f.readline().strip()
        f.close()

        print self.ADDR, self.PORT

        self.login()


    def login(self):
        print "logging in to ISY..."
        self.session = PyISY.ISY(self.ADDR, self.PORT, self.USER, self.PASS)

    def getStatus(self):
        return self.session.connected

    def setNode(self, nid, on=True):
        if(on):
            self.session.nodes[nid].on()
        else:
            self.session.nodes[nid].off()
        
        


