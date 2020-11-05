
from persistence import reader

settings = reader.read_settings('../settings.csv')
outcomes = reader.read_outcomes('../outcomes.csv')
groups = reader.read_groups('../groups.csv','../outcomes.csv')
plots = reader.read_plots('../plots.csv', '../groups.csv','../outcomes.csv')

print('settings')
for setting in settings:
    print(setting.to_string())
print('\n\n outcomes')
for outcome in outcomes:
    print(outcome.to_string())
print('\n\n groups')
for group in groups:
    print(group.to_string())
print('\n\n plots')
for plot in plots:
    print(plot.to_string())
