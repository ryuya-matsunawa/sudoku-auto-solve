# -*- coding: utf-8 -*-
from itertools import product
from select import select
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import FocusBehavior
import solve

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

    # def on_press(self):
    #     self.selected_cell = self.ce
    #     with self.canvas.before:
    #         Color(1, 1, 0, 2) # yellow; colors range from 0-1 instead of 0-255
    #         Rectangle(pos=self.pos, size=self.size) # set a rectangle as the background

class SudokuApp(App):
    def __init__(self, **kwargs):
        super(SudokuApp, self).__init__(**kwargs)

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
            cell.fbind("on_press", self.change_cell)
            cell.text = Cell.DIC[index]
            number_grid.add_widget(cell)
        # return main_grid

    def select_cell(self, cell, pos):
        if self.selected_cell is not None:
            self.selected_cell.canvas.before.clear()
        self.selected_cell = cell
        self.selected_cell_pos = pos
        with cell.canvas.before:
            Color(1, 1, 0, 2)
            Rectangle(pos=cell.pos, size=cell.size)

    def change_cell(self, cell):
        self.cells[self.selected_cell_pos].text = cell.text

    def solve(self):
        problem = [[0] * 9 for _ in range(9)]
        for (i, j) in product(range(3), repeat=2):
            cell = self.cells[(i, j)].text
            problem[i][j] = int(cell) if cell != "*" else 0
        answers = solve.main(problem)
        for (i, j) in product(range(9), repeat=2):
            self.cells[(i, j)].text = Cell.DIC[answers[0][i][j]]
        pass

    def reset(self):
        for (i, j) in product(range(9), repeat=2):
            self.cells[(i, j)].text = Cell.DIC[0]

if __name__ == '__main__':
    SudokuApp().run()