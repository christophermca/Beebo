class Beebo:

    def __init__(self):
        self.ctnr = []
        self.on()
        self.coords = [0, 0]

    def get_status(self):
        return vars(self)

    def on(self):
        self.heartbeat = True

    def off(self):
        self.heartbeat = False

    def movement(self, y, x):
        if(y is not self.coords[0] or x is not self.coords[1]):
            self.coords(y, x)

    def pick_up_item(self, item):
        if (item and len(self.ctnr) == 0):
            self.ctnr.append(item)
        else:
            raise Exception("Cannot pick that up")

    def drop_item(self):
        if (len(self.ctnr) == 1):
            item = self.ctnr.pop()
            return item
        else:
            raise Exception("No Items in container")

    heartbeat = None
