from persistence import writer
from persistence import reader
from utils import execute
from model.group import Group

SETTINGS_FILE_NAME = 'settings.csv'
SERVICE_FILE_NAME = 'out/service_file.csv'
GROUPS_FILE_NAME = 'out/groups.csv'

def save(configs=None):
    #Non ci sono contolli
    if configs==None or len(configs)==0:
        configs = reader.read_configs(SETTINGS_FILE_NAME)
    writer.write_configs(SETTINGS_FILE_NAME,configs)

def run(configs=None):
    if configs==None or len(configs)==0:
        configs = reader.read_configs(SETTINGS_FILE_NAME)
    output_file = writer.get_service_file(SERVICE_FILE_NAME)
    execute.exec(configs,output_file)
    output_file.close()
    groups = Group.get_groups(reader.read_services(SERVICE_FILE_NAME))
    writer.write_groups(GROUPS_FILE_NAME,groups)
