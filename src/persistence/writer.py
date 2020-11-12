OUTCOME_FILE = '../../outcome.csv'


def write_settings(settings_filename, settings):
    file = open(settings_filename, "w")
    for setting in settings:
        file.write(setting.to_string() + '\n')
    file.close()


def write_outcomes(outcomes_filename, outcomes):
    file = open(outcomes_filename, "w")
    for outcome in outcomes:
        file.write(outcome.to_string() + '\n')
    file.close()


def write_outcome(outcomes_file, outcome):
    outcomes_file.write(outcome.to_string() + '\n')


def get_outcome_file(outcome_filename=OUTCOME_FILE):
    return open(outcome_filename, "a")


def write_groups(groups_filename, groups):
    file = open(groups_filename, "w")
    for group in groups:
        file.write(group.to_string() + '\n')
    file.close()


def write_plots(plots_filename, plots):
    file = open(plots_filename, "w")
    for plot in plots:
        file.write(plot.to_string() + '\n')
    file.close()
