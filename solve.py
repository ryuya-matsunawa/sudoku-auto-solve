from itertools import product

def main(problem):
    for (i, j) in product(range(9), repeat=2):
        if problem[i][j] == 0:
            problem[i][j] = 1
    return problem

if __name__ == '__main__':
    main()