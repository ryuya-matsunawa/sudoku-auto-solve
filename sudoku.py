# -*- coding: utf-8 -*-
from itertools import product
from select import select
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import FocusBehavior

# from kivy.lang import Builder
# Builder.load_file('./sudoku.kv')

class MainGrid(FocusBehavior, GridLayout):
    pass
    def __init__(self, **kwargs):
        super(MainGrid, self).__init__(**kwargs)

class SubGrid(GridLayout):
    def __init__(self, **kwargs):
        super(SubGrid, self).__init__(**kwargs)

class Cell(Button):
    DIC = {0: "*", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

    def __init__(self, **kwargs):
        super(Cell, self).__init__(**kwargs)
        self.text = Cell.DIC[0]

class SudokuApp(App):
    def __init__(self, **kwargs):
        super(SudokuApp, self).__init__(**kwargs)

    def build(self):
        main_grid = self.root.ids.main_grid
        for (k, l) in product(range(3), repeat=2):
            sub_grid = SubGrid()
            for (i, j) in product(range(3), repeat=2):
                cell = Cell()
                sub_grid.add_widget(cell)
            main_grid.add_widget(sub_grid)
        # return main_grid

if __name__ == '__main__':
    SudokuApp().run()