class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state

class Messybot(Borg):
    def __init__(self):
        Borg.__init__(self)

    def has_key(self, key):
        if key in self.__dict__:
            return True
        else:
            return False
 	
