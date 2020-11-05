from model.group import Group
from model.outcome import Outcome
from model.plot import Plot
from model.setting import Setting
from persistence import writer

s0 = Setting(0, "version", "name", "path", "filename", "extension", "args", "stdin", 1, 1,
             True, 1, 1)
s1 = Setting(1, "version1", "name1", "path1", "filename", "extension", "args", "stdin")
s2 = Setting(2, "version2", "name2", "path2", "filename", "extension", "args", "stdin", 1, 1,
             True)

writer.write_settings('../settings.csv', [s0, s1, s2])

o0 = Outcome(0, 0.01230)
o1 = Outcome(0, 0.1131231)
o2 = Outcome(0, 0.3231230)

o00 = Outcome(1, 0.121231230)
o01 = Outcome(1, 0.1113123)
o02 = Outcome(1, 0.321231230)

outcomes = [o0, o1, o2, o00, o01, o02]

outcomes_file = writer.get_outcome_file('../outcomes.csv')
writer.write_outcome(outcomes_file, o0)
writer.write_outcome(outcomes_file, o1)
outcomes_file.close()

writer.write_outcomes('../outcomes.csv', outcomes)

groups = Group.get_groups(outcomes)
groups.append(Group(2, outcomes, [255, 255, 255], True, False))
groups.append(Group(3, outcomes, [255, 255, 255], True, False))
groups.append(Group(5, outcomes, [255, 255, 255], True, False))

writer.write_groups('../groups.csv', groups)

plots = list()
plots.append(Plot(0, groups))

groups = []
groups.append(Group(8, outcomes, [255, 255, 255], True, False))
groups.append(Group(3, outcomes, [255, 255, 255], True, False))
groups.append(Group(1, outcomes, [255, 255, 255], True, False))
plots.append(Plot(1, groups))

writer.write_plots('../plots.csv', plots)
