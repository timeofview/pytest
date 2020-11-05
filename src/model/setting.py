class Setting:
    def __init__(self, id, version, name, path, filename, extension, args, stdin, threads=1, iterations=1,
                 concurrency=True, s_timestamp=1, d_graphs=1):
        self.id = id
        self.version = version
        self.name = name
        self.path = path
        self.filename = filename
        self.extension = extension
        self.args = args
        self.stdin = stdin
        self.threads = threads
        self.iterations = iterations
        self.concurrency = concurrency
        self.s_timestamp = s_timestamp
        self.d_graphs = d_graphs

    def to_string(self):
        setting = map(lambda x: str(x), vars(self).values())
        return ','.join(setting)
