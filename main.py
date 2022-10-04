# -*- coding: utf-8 -*-
from itertools import product
from select import select
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
import solve

class MainGrid(GridLayout):
    pass

class SubGrid(GridLayout):
    pass

class Cell(Button):
    DIC = {0: "*", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

    def __init__(self, **kwargs):
        super(Cell, self).__init__(**kwargs)
        self.text = Cell.DIC[0]

class SudokuApp(App):
    def build(self):
        self.cells = dict()
        main_grid = self.root.ids.main_grid
        for (k, l) in product(range(3), repeat=2):
            sub_grid = SubGrid()
            for (i, j) in product(range(3), repeat=2):
                cell = Cell()
                self.selected_cell = None
                cell.fbind("on_press", self.select_cell, pos=(k*3+i, l*3+j))
                self.cells[(3*k+i, 3*l+j)] = cell
                sub_grid.add_widget(cell)
            main_grid.add_widget(sub_grid)
        number_grid = self.root.ids.number_grid
        for index in range(1, 10):
            cell = Cell()
            cell.fbind("on_press", self.set_number)
            cell.text = Cell.DIC[index]
            number_grid.add_widget(cell)

    def select_cell(self, instance, pos):
        if self.selected_cell is not None:
            self.selected_cell.background_color = (1, 1, 1, 1)
        self.selected_cell = instance
        self.selected_cell_pos = pos
        self.selected_cell.background_color = (0, 1, 0, 1)

    def set_number(self, instance):
        if self.selected_cell:
            self.cells[self.selected_cell_pos].text = instance.text

    def solve(self):
        problem = [[0] * 9 for _ in range(9)]
        for (i, j) in product(range(9), repeat=2):
            cell = self.cells[(i, j)].text
            problem[i][j] = int(cell) if cell != "*" else 0
        answers = solve.main(problem)
        for (i, j) in product(range(9), repeat=2):
            self.cells[(i, j)].text = Cell.DIC[answers[0][i][j]]

    def reset(self):
        solve.answers = []
        for (i, j) in product(range(9), repeat=2):
            self.cells[(i, j)].text = Cell.DIC[0]

if __name__ == '__main__':
    SudokuApp().run()