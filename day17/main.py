from itertools import product
import numpy as np


def update(grid):
    subGrid = np.zeros([d + 2 for d in grid.shape])
    subGrid[(slice(1, -1),) * grid.ndim] = grid

    gridBack = subGrid
    gridBack1 = gridBack.copy()
    for pos in [*product(*[range(d) for d in gridBack.shape])]:

        s = [slice(max(x - 1, 0), x + 2) for x in pos]
        neighbors = gridBack[tuple(s)].sum()


        if gridBack[pos] == 0 and neighbors == 3:
            gridBack1[pos] = 1
        if gridBack[pos] == 1 and neighbors<3 or neighbors > 4:
            gridBack1[pos] = 0

    return gridBack1


def day17_1(grid, nbGen, dim):
    gridBackup = grid.copy()[(...,) + (None,) * (dim - grid.ndim)]
    for i in range(0, nbGen):
        gridBackup = update(gridBackup)
    return gridBackup.sum()


if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    linesDeMonFichier = fichier.read()

    grid = np.array([[1 if v == "#" else 0 for v in line] for line in linesDeMonFichier.splitlines()])
    print(grid)
    print(day17_1(grid, 6, 3))
    print(day17_1(grid, 6, 4))
