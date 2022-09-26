# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from kivy.lang import Builder
Builder.load_file('./SampleGrid.kv')

class MyGrid1(GridLayout):
    pass

class SampleGridLayoutApp(App):
    def build(self):
        root = MyGrid1()
        return root

if __name__ == '__main__':
    SampleGridLayoutApp().run()