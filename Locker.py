#class that represents locker object

class Locker():
    def __init__(self, locker_id, locker_pin):
        self.locker_id = locker_id
        self.status = 0    #0 - locker is closed at the moment, 1 - opened
        self.locker_pin = locker_pin

    def do_action(self, action):
        if action == "open":
            #TODO open the locker
            pass
        elif action == "close":
            #TODO close the locker
            pass