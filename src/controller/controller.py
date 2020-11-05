from persistence import writer
from persistence import reader
from utils import threads_manager
from utils import draw


SETTINGS_FILENAME = 'settings.csv'
OUTCOMES_FILENAME = 'out/service_file.csv'
GROUPS_FILENAME = 'out/groups.csv'
PLOTS_FILENAME = 'out/groups.csv'

def save_settings(settings):
    if settings!=None or len(settings)>0:
        writer.write_settings(SETTINGS_FILENAME, settings)

def run(settings=None):
    if settings==None or len(settings)==0:
        settings = reader.read_settings(SETTINGS_FILENAME)
    output_file = writer.get_settings_file(OUTCOMES_FILENAME)
    threads_manager.exec(settings, output_file)
    output_file.close()

def save_groups(groups,plots):
    if groups!=None and len(groups)>0 and plots!=None and len(plots)>0:
        writer.write_groups(GROUPS_FILENAME,groups)
        writer.write_plots(PLOTS_FILENAME,plots)

def read_plots():
    return reader.read_plots(PLOTS_FILENAME,GROUPS_FILENAME,OUTCOMES_FILENAME)

def read_settings():
    return reader.read_settings(SETTINGS_FILENAME)

def draw(plots):
    #TODO
    #manca draws
    print()