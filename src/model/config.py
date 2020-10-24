class Config:
    def __init__(self, version, name, path, filename,extension, args, threads, stdin, s_timestapm=1, d_graphs=1):
        self.version = version
        self.name = name
        self.path = path
        self.filename = filename
        self.extension = extension
        self.args = args
        self.thread = threads
        self.stdin = stdin
        self.s_timestapm = str(s_timestapm)
        self.d_graphs = str(d_graphs)
    def toString(self):
        return ','.join(vars(self).values())
