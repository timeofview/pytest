from kivy.uix.boxlayout import BoxLayout


class Row(BoxLayout):
    def __init__(self, list):
        super(Row,self)
        for el in list:
            self.add_widget(el)
        self.list = list

    def get_list(self):
        return list
