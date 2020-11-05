import random


class Group():
    def __init__(self, id, outcomes, color=[0, 0, 255], draw_templates=True, draw_avg=True):
        self.id = int(id)
        self.outcomes = outcomes
        self.draw_templates = bool(draw_templates)
        self.draw_avg = bool(draw_avg)
        self.color = color

    @staticmethod
    def get_groups(outcomes):
        id = 0
        groups = list()
        for outcome0 in outcomes:
            group_outcomes = list()
            for outcome1 in outcomes:
                if outcome0.id == outcome1.id:
                    group_outcomes.append(outcome1)
                    if outcome1 in outcomes:
                        outcomes.remove(outcome1)
                    if outcome0 in outcomes:
                        outcomes.remove(outcome0)
            groups.append(Group(id, group_outcomes))
            id += 1
        return groups

    @staticmethod
    def random_color():
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)
        return tuple(rgbl)

    def to_string(self):
        return ','.join(
            [str(self.id), str(self.outcomes[0].id), str(self.draw_templates), str(self.draw_avg), ','.join(str(e) for e in self.color)])
