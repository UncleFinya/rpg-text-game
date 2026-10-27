class Game:
    def __init__(self):
        self.listeners = []

    def subsribe(self, callback):
        self.listeners.append(callback)

    def _emit(self, event, data):
        for cb in self.listeners:
            cb(event, data)