from kivy.app import App
from kivy.graphics.svg import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem

from components.row import SettingRow
from controller.controller import Controller
from components.table import TableSettings
from model.setting import Setting


class Tab(TabbedPanel):
    pass


class UI(App):
    def build(self):
        height = 800
        width = 1000

        settings_layout = GridLayout(cols=2)

        self.my_controller = Controller()

        self.settings_table = TableSettings(self.my_controller)
        settings_layout.add_widget(self.settings_table.get_table())
        add_button = Button(text='add', size_hint=(.09, .005))
        add_button.bind(on_press=self.add_setting)
        settings_layout.add_widget(add_button)
        settings = TabbedPanelItem(text='settings')
        settings.add_widget(settings_layout)

        tp = TabbedPanel()
        tp.add_widget(settings)

        groups_layout = GridLayout()
        groups = TabbedPanelItem(text='groups')
        groups.add_widget(groups_layout)

        tp.add_widget(groups)

        # tp.set_def_tab(settings)
        Window.clearcolor = (.43, .43, .43, .01)
        Window.size = (width, height)

        return settings_layout

    def add_setting(self,instance):
        #TODO
        self.settings_table.add_setting()

    def save_settings(self,instance):
        self.my_controller.save_settings()

def main():
    UI().run()


if __name__ == "__main()__":
    main()

main()
