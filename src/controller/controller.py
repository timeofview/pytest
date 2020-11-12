import os

from persistence import writer
from persistence import reader
from utils import threads_manager
from model.setting import Setting
from model.plot import Plot
from utils import draw

SETTINGS_FILENAME = '../../out/settings.csv'
OUTCOMES_FILENAME = '../../out/outcome.csv'
GROUPS_FILENAME = '../../out/groups.csv'
PLOTS_FILENAME = '../../out/plots.csv'


class Controller():
    def __init__(self):
        self.settings = self.read_settings()
        self.plots = self.read_plots()

    def get_settings(self):
        return self.settings

    def set_settings(self, settings):
        self.settings = settings

    def get_setting_from_row(self, name, version, path, args, stdin, threads, iterations, concurrency, s_timestamp):
        setting = Setting(id=(self.settings[len(self.settings) - 1].id + 1), version=version,
                          path=os.path.dirname(path),
                          name=name,
                          filename=os.path.basename(path).split('.')[0], extension=os.path.splitext(path)[1], args=args,
                          stdin=stdin,
                          threads=int(threads), iterations=int(iterations), concurrency=bool(concurrency),
                          s_timestamp=bool(s_timestamp))
        # FIXME
        self.settings.append(setting)
        return setting

    def add_setting(self, name='', version='', path='', args='', stdin='', threads=1, iterations=1, s_timestamp=True):
        self.settings.append(
            Setting(id=(self.settings[len(self.settings) - 1].id + 1), version=version, name=name,
                    path='\\'.join(path.split('\\')[0:-1]),
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
        output_file = writer.get_outcome_file(OUTCOMES_FILENAME)
        threads_manager.exec(settings, output_file)
        output_file.close()

    def save_groups(self, plots):
        groups = plots.groups
        if groups != None and len(groups) > 0 and plots != None and len(plots) > 0:
            writer.write_groups(GROUPS_FILENAME, groups)
            writer.write_plots(PLOTS_FILENAME, plots)

    def read_plots(self):
        return reader.read_plots(PLOTS_FILENAME, GROUPS_FILENAME, OUTCOMES_FILENAME)

    def update_plot(self, plot_id, group_id, color, draw_templates, draw_avg):

        for p in self.plots:
            for g in p.groups:
                if g.id == group_id:
                    p.groups.remove(g)
                    break

        founded = False
        g.set_color(color)
        g.set_draw_templates(draw_templates)
        g.set_draw_avg(draw_avg)

        for p in self.plots:
            if p.id == plot_id:
                founded = True
                p.groups.append(g)
                break
        if not founded:
            self.plots(Plot(id=(self.plots[len(self.plots) - 1].id + 1)),list(g))


    def read_settings(self):
        return reader.read_settings(SETTINGS_FILENAME)

    def draw(self, plots):
        # TODO
        # manca draws
        print()
