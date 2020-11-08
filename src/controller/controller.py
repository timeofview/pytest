import os

from persistence import writer
from persistence import reader
from utils import threads_manager
from model.setting import Setting
from utils import draw

SETTINGS_FILENAME = '../../test/settings.csv'
OUTCOMES_FILENAME = 'out/service_file.csv'
GROUPS_FILENAME = 'out/groups.csv'
PLOTS_FILENAME = 'out/groups.csv'


class Controller():
    def __init__(self):
        self.settings = self.read_settings()

    def get_settings(self):
        return self.settings

    def add_setting(self, name='', version='', path='', args='', stdin='', threads=1, iterations=1, s_timestamp=True):
        self.settings.append(
            Setting(id=self.settings[len(self.settings) - 1], version=version, path='\\'.join(path.split('\\')[0:-1]),
                    filename=os.path.basename(path), extension=os.path.splitext(path)[1], args=args, stdin=stdin,
                    threads=int(threads), iterations=int(iterations), s_timestamp=bool(s_timestamp)))

    def save_settings(self, settings=None):
        if (settings == None):
            settings = self.settings
        if len(settings) > 0:
            writer.write_settings(SETTINGS_FILENAME, settings)

    def run(self, settings=None):
        if settings == None or len(settings) == 0:
            settings = reader.read_settings(SETTINGS_FILENAME)
        output_file = writer.get_settings_file(OUTCOMES_FILENAME)
        threads_manager.exec(settings, output_file)
        output_file.close()

    def save_groups(self, groups, plots):
        if groups != None and len(groups) > 0 and plots != None and len(plots) > 0:
            writer.write_groups(GROUPS_FILENAME, groups)
            writer.write_plots(PLOTS_FILENAME, plots)

    def read_plots(self):
        return reader.read_plots(PLOTS_FILENAME, GROUPS_FILENAME, OUTCOMES_FILENAME)

    def read_settings(self):
        return reader.read_settings(SETTINGS_FILENAME)

    def draw(self, plots):
        # TODO
        # manca draws
        print()
