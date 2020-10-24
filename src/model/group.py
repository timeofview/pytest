class Group():
    def __init__(self, groupid, subgroupid, version, name, threads, stdin, draw_templates=1, draw_avg=1,
                 color='#32a852'):
        self.groupid = str(groupid)
        self.subgroupid = str(subgroupid)
        self.version = version
        self.name = name
        self.thread = threads
        self.stdin = stdin
        self.draw_templates = str(draw_templates)
        self.draw_avg = str(draw_avg)
        self.color = color

    @staticmethod
    def group_by(services):
        result = list()
        for s0 in services:
            tmp = list()
            tmp.append(s0)
            services.remove(s0)
            for s1 in services:
                if s0.name == s1.name and s0.version == s1.version and s0.threads == s1.threads and s0.stdin == s1.stdin:
                    tmp.append(s1)
                    services.remove(s1)
            result.append(tmp)
        return result

    @staticmethod
    def get_groups(groupedBy):
        result = list()
        subgroupid=0
        for group in groupedBy:
            result.append(Group(0,subgroupid,group[0].version,group[0].name,group[0].threads,group[0].stdin))
            subgroupid+=1
        return result


    def to_string(self):
        return ','.join(vars(self).values())
