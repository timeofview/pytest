from model.group import Group
from model.outcome import Outcome
from model.plot import Plot

o0 = Outcome(0, 0.1230)
o1 = Outcome(0, 0.113)
o2 = Outcome(0, 0.3230)

o00 = Outcome(1, 0.1230)
o01 = Outcome(1, 0.113)
o02 = Outcome(1, 0.3230)

outcomes = [o0,o1,o2,o00,o01,o02]

groups = Group.get_groups(outcomes)
groups.append(Group(2,outcomes,[255,255,255],True,False))
groups.append(Group(3,outcomes,[255,255,255],True,False))
groups.append(Group(5,outcomes,[255,255,255],True,False))

plots = list()
plots.append(Plot(0,groups))

groups = []
groups.append(Group(8,outcomes,[255,255,255],True,False))
groups.append(Group(3,outcomes,[255,255,255],True,False))
groups.append(Group(1,outcomes,[255,255,255],True,False))

plots.append(Plot(1,groups))

for plot in plots:
    res = plot.to_string()
    print(plot.to_string())