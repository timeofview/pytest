class Outcome:
    def __init__(self, id, timestamp):
        self.id = int(id)
        self.timestamp = float(timestamp)

    def to_string(self):
        return str(self.id)+","+str(self.timestamp)
