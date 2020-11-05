class Plot:
    def __init__(self, id, groups):
        self.id = int(id)
        self.groups = groups

    def to_string(self):
        group_ids = map(lambda group: str(group.id), self.groups)
        return str(self.id) + ',' + ','.join(group_ids)
