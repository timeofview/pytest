from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from model.setting import Setting


class SettingRow:
    def __init__(self, setting):
        self._disabled_count = 0
        self.setting = setting
        self.row = BoxLayout( size_hint=(.9, .1))
        self.set_setting(setting)

    def set_setting(self, setting):
        self.row.add_widget(TextInput(text=setting.name))
        self.row.add_widget(TextInput(text=setting.version))
        self.row.add_widget(TextInput(text=(setting.path + setting.filename + setting.extension)))
        self.row.add_widget(TextInput(text=setting.args))
        self.row.add_widget(TextInput(text=setting.stdin))
        self.row.add_widget(TextInput(text=str(setting.threads)))
        self.row.add_widget(TextInput(text=str(setting.iterations)))
        self.row.add_widget(CheckBox(active=setting.s_timestamp))


    def get_row(self):
        return self.row
