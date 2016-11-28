import sys
sys.path.insert(0, '/home/provolot/_GITHUB/PyISY')
sys.path.insert(0, '/Users/provolot/github/PyISY')
import PyISY

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

    def get_status(self):
        return self.isy.connected

    def set_node(self, nid, on=True):
        if(on):
            self.isy.nodes[nid].on()
        else:
            self.isy.nodes[nid].off()

    def current_temp(self):
        self.isy.nodes['ZW003_1'].update()
        return self.isy.nodes['ZW003_1'].status

    @property
    def heatpoint(self):
        return self.isy.nodes['ZW003_1'].property('CLISPH')['value']
    @heatpoint.setter
    def heatpoint(self, value):
        return self.isy.nodes['ZW003_1'].property('CLISPH', str(value))
   

