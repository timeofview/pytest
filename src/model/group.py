import random


class Group():
    def __init__(self, groupid, subgroupid, services, draw_templates=1, draw_avg=1,
                 color=[255,0,0]):
        self.groupid = str(groupid)
        self.subgroupid = str(subgroupid)
        self.services = services
        self.draw_templates = str(draw_templates)
        self.draw_avg = str(draw_avg)
        self.color = color

    @staticmethod
    def get_groups(services):
        subgroupid=0
        groups = list()
        for s0 in services:
            services = list()
            services.append(s0)
            services.remove(s0)
            for s1 in services:
                if s0.name == s1.name and s0.version == s1.version and s0.threads == s1.threads and s0.stdin == s1.stdin:
                    services.append(s1)
                    services.remove(s1)
            groups.append(Group(0,subgroupid,services,1,1,Group.random_color()))
            subgroupid+=1
        return groups

    @staticmethod
    def random_color():
        rgbl=[255,0,0]
        random.shuffle(rgbl)
        return tuple(rgbl)

    def to_string(self):
        return ','.join([self.groupid,self.subgroupid,self.draw_templates,self.draw_avg,str(self.color)])
