from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from .row import SettingRow


class TableSettings:
    def __init__(self, controller):
        self.controller = controller
        self.table = BoxLayout(orientation='vertical')
        self.rows = list()
        self.set_settings()
        self.labels = BoxLayout(size_hint=(.9, .05))
        self.labels.add_widget(Label(text='Name'))
        self.labels.add_widget(Label(text='Version'))
        self.labels.add_widget(Label(text='Path'))
        self.labels.add_widget(Label(text='Args'))
        self.labels.add_widget(Label(text='Stdin'))
        self.labels.add_widget(Label(text='Threads'))
        self.labels.add_widget(Label(text='Iterations'))
        self.labels.add_widget(Label(text='Save timestamp'))
        self.update_rows()

    def set_settings(self ):
        for setting in self.controller.get_settings():
            self.rows.append(SettingRow(setting))

    def add_setting(self, setting):
        self.controller.add_setting(setting)
        row = SettingRow(setting)
        self.rows.append(row)
        self.table.add_widget(row)

    def update_rows(self):
        self.table.add_widget(self.labels)
        for row in self.rows:
            self.table.add_widget(row.get_row())

    def get_table(self):
        return self.table
