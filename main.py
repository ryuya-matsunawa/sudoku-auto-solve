# -*- coding: utf-8 -*-
from itertools import product
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from kivy.lang import Builder
Builder.load_file('./SampleGrid.kv')

class MainGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MainGrid, self).__init__(**kwargs)

class SubGrid(GridLayout):
    def __init__(self, **kwargs):
        super(SubGrid, self).__init__(**kwargs)

class Cell(Button):
    def __init__(self, **kwargs):
        super(Cell, self).__init__(**kwargs)
        self.text = '0'

class SudokuApp(App):
    def __init__(self, **kwargs):
        super(SudokuApp, self).__init__(**kwargs)

    def build(self):
        main_grid = MainGrid()
        for (k, l) in product(range(3), repeat=2):
            sub_grid = SubGrid()
            for (i, j) in product(range(3), repeat=2):
                cell = Cell()
                cell.text = str(i)
                # self.cells[(3*k+i, 3*l+j)] = cell
                sub_grid.add_widget(cell)
            main_grid.add_widget(sub_grid)
        return main_grid

if __name__ == '__main__':
    SudokuApp().run()