import math


def rotate(value, pos):
    x = pos[1][0] * math.cos(math.radians(value)) - pos[1][1] * math.sin(math.radians(value))
    y = pos[1][0] * math.sin(math.radians(value)) + pos[1][1] * math.cos(math.radians(value))

    return [int(round(x, 0)), int(round(y))]


def N(value, pos):
    return [[pos[0][0], pos[0][1] + value], pos[1]]


def S(value, pos):
    return [[pos[0][0], pos[0][1] - value], pos[1]]


def E(value, pos):
    return [[pos[0][0] + value, pos[0][1]], pos[1]]


def W(value, pos):
    return [[pos[0][0] - value, pos[0][1]], pos[1]]


def L(value, pos):
    v = rotate(value, pos)
    return [pos[0], v]


def R(value, pos):
    v = rotate(-value, pos)
    return [pos[0], v]


def F(value, pos):
    return [[pos[0][0] + pos[1][0] * value, pos[0][1] + pos[1][1] * value], pos[1]]


def day12_2(data, start):
    for i in data:

        if i[0] in 'NSEW':
            v2 = globals()[i[0]](i[1], [start[1], start[0]])
            start[1][0] = v2[0][0]
            start[1][1] = v2[0][1]
        elif i[0] in 'RL':
            v2 = globals()[i[0]](i[1], start)
            start[1][0] = v2[1][0]
            start[1][1] = v2[1][1]
        else:
            start[0][0] += start[1][0] * i[1]
            start[0][1] += start[1][1] * i[1]
        print(i, start)
    return start


def day12_1(data, start):
    for i in data:
        start = globals()[i[0]](i[1], start)

    return start


# main
if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    linesDeMonFichier = fichier.read().splitlines()

    data = [[d[0], int(d[1:])] for d in linesDeMonFichier]

    r = day12_1(data, [[0, 0], [1, 0]])
    print(abs(r[0][0]) + abs(r[0][1]))

    r = day12_2(data, [[0, 0], [10, 1]])
    print(abs(r[0][0]) + abs(r[0][1]))
