import copy
from itertools import product

def main(problem):
    answer = copy.deepcopy(problem)
    if solve(answer, 0, 0):
        return answer

def solve(problem, row, col):
    if row == 9:
        return True
    if col == 9:
        return solve(problem, row + 1, 0)
    if problem[row][col] != 0:
        return solve(problem, row, col + 1)
    for k in range(1, 10):
        if check(problem, row, col, k):
            problem[row][col] = k
            if solve(problem, row, col + 1):
                return True
            problem[row][col] = 0
    return False

def check(problem, row, col, k):
    for i in range(9):
        if problem[row][i] == k:
            return False
        if problem[i][col] == k:
            return False
    for (i, j) in product(range(3), repeat=2):
        if problem[row//3*3+i][col//3*3+j] == k:
            return False
    return True

if __name__ == '__main__':
    main()