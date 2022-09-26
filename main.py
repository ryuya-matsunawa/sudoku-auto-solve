# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from kivy.lang import Builder
Builder.load_file('./SampleGrid.kv')

class MainGrid(GridLayout):
    pass

class SudokuApp(App):
    def build(self):
        root = MainGrid()
        return root

if __name__ == '__main__':
    SudokuApp().run()