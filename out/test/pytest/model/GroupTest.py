from model.group import Group
from model.outcome import Outcome

o0 = Outcome(0, 0.1230)
o1 = Outcome(0, 0.113)
o2 = Outcome(0, 0.3230)

o00 = Outcome(1, 0.1230)
o01 = Outcome(1, 0.113)
o02 = Outcome(1, 0.3230)

outcomes = [o0,o1,o2,o00,o01,o02]

groups = Group.get_groups(outcomes)
if len(groups)==2:
    print('ok');

print(str(Group.random_color()))
print(str(Group.random_color()))
print(str(Group.random_color()))

groups.append(Group(2,outcomes,[255,255,255],True,False))

for group in groups:
    print(group.to_string())