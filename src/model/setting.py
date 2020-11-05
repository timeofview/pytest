class Setting:
    def __init__(self, id, version, name, path, filename, extension, args, stdin, threads=1, iterations=1,
                 concurrency=True, s_timestamp=1, d_graphs=1):
        self.id = int(id)
        self.version = version
        self.name = name
        self.path = path
        self.filename = filename
        self.extension = extension
        self.args = args
        self.stdin = stdin
        self.threads = int(threads)
        self.iterations = int(iterations)
        self.concurrency = bool(concurrency)
        self.s_timestamp = bool(s_timestamp)
        self.d_graphs = bool(d_graphs)

    def to_string(self):
        setting = map(lambda x: str(x), vars(self).values())
        return ','.join(setting)
