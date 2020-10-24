class Service():
    def __init__(self, version, name, args, threads, stdin, timestamp, s_timestapm=1, d_graphs=1):
        self.version = version
        self.name = name
        self.args = args
        self.thread = threads
        self.stdin = stdin
        self.timestamp = "%.20f" % timestamp
        self.s_timestapm = str(s_timestapm)
        self.d_graphs = str(d_graphs)

    def to_string(self):
        return ','.join(vars(self).values())