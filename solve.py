import copy
from itertools import product

answers = []

def main(problem):
    if solve(problem, 0, 0):
        answers.append(problem)
        return answers

def solve(problem, row, col):
    if row == 9:
        return True
    if col == 9:
        return solve(problem, row + 1, 0)
    if problem[row][col] != 0:
        return solve(problem, row, col + 1)
    for num in range(1, 10):
        if check(problem, row, col, num):
            problem[row][col] = num
            if solve(problem, row, col + 1):
                return True
            problem[row][col] = 0
    return False

def check(problem, row, col, num):
    for i in range(9):
        if problem[row][i] == num:
            return False
        if problem[i][col] == num:
            return False
    for (i, j) in product(range(3), repeat=2):
        if problem[row//3*3+i][col//3*3+j] == num:
            return False
    return True

if __name__ == '__main__':
    main()