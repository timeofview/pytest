class Outcome:
    def __init__(self, id, timestamp):
        self.id = id
        self.timestamp = timestamp

    def to_string(self):
        return str(self.id)+","+str(self.timestamp)
