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
        width = 1200

        settings_layout = GridLayout(cols=2)

        self.my_controller = Controller()

        self.settings_table = TableSettings(self.my_controller)
        settings_layout.add_widget(self.settings_table.get_table())
        add_button = Button(text='add', size_hint=(.09, .005))
        add_button.bind(on_press=self.add_setting)
        save_and_run = GridLayout(cols=2)
        save_button = Button(text='Save', size_hint=(.09, .005))
        save_button.bind(on_press=self.save_settings)
        run_button = Button(text='Run', size_hint=(.09, .005))
        run_button.bind(on_press=self.run_settings)
        save_and_run.add_widget(save_button)
        save_and_run.add_widget(run_button)
        settings_layout.add_widget(add_button)
        settings_layout.add_widget(save_and_run)
        settings = TabbedPanelItem(text='settings')
        settings.add_widget(settings_layout)
        tp = TabbedPanel()
        tp.add_widget(settings)

        groups_layout = GridLayout()
        groups = TabbedPanelItem(text='groups')
        groups.add_widget(groups_layout)

        tp.add_widget(groups)

        tp.set_def_tab(settings)
        Window.clearcolor = (.43, .43, .43, .01)
        Window.size = (width, height)

        return tp

    def add_setting(self, instance):
        # TODO
        self.settings_table.add_setting()

    def save_settings(self, instance):
        self.settings_table.update_settings()
        self.my_controller.save_settings()

    def run_settings(self, instance):
        self.my_controller.run()


def main():
    UI().run()


if __name__ == "__main()__":
    main()

main()
