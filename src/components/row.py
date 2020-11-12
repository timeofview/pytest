from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput


class SettingRow:
    def __init__(self, setting):
        self.setting = setting
        self.row = BoxLayout(size_hint=(.9, .1))
        self.set_setting(setting)

    def set_setting(self, setting):
        self.row.add_widget(TextInput(text=setting.name))
        self.row.add_widget(TextInput(text=setting.version))
        self.row.add_widget(TextInput(text=(setting.path + '/' + setting.filename + setting.extension)))
        self.row.add_widget(TextInput(text=setting.args))
        self.row.add_widget(TextInput(text=setting.stdin))
        self.row.add_widget(TextInput(text=str(setting.threads)))
        self.row.add_widget(TextInput(text=str(setting.iterations)))
        self.row.add_widget(CheckBox(active=setting.concurrency))
        self.row.add_widget(CheckBox(active=setting.s_timestamp))

    def get_row(self):
        return self.row

    def get_children(self):
        return self.row.children


class GroupRow:
    def __init__(self, group):
        self.group = group
        self.row = BoxLayout(size_hint=(.9, .1))
        self.set_setting(group)

    def set_group(self, plot_id, group):
        self.row.add_widget(TextInput(text=plot_id))
        self.row.add_widget(TextInput(text=group.id))
        self.row.add_widget(TextInput(text=group.color))
        self.row.add_widget(CheckBox(active=group.draw_templates))
        self.row.add_widget(CheckBox(active=group.draw_avgs))

    def get_row(self):
        return self.row

    def get_children(self):
        return self.row.children
