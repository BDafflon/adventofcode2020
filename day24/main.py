import regex

from sys import stdin
from functools import reduce
from collections import Counter




def parse(l):
    res = []
    while l:
        for d in ['e', 'se', 'sw', 'w', 'nw', 'ne']:
            if l.startswith(d):
                res += [d]
                l = l[len(d):]
    return res


def move(xyz, dirs):
    def step(x, y, z, d): return {
        'e':  (x-1, y+1, z),
        'w':  (x+1, y-1, z),
        'se': (x, y+1, z-1),
        'sw': (x+1, y, z-1),
        'nw': (x, y-1, z+1),
        'ne': (x-1, y, z+1)
    }[d]
    return reduce(lambda xyz, d: step(*xyz, d),
                  dirs, xyz)


def flip(blacks):
    neighbours = Counter(move(t, [d]) for d in ['e', 'se', 'sw', 'w', 'nw', 'ne'] for t in blacks)
    blacks = set(t for t, val in neighbours.items()
                 if val == 2 or t in blacks and val == 1)
    return blacks



def day24_1():
    pass


if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    data = fichier.read().split('\n')

    blacks = set()
    for d in [parse(l.strip()) for l in data]:
        if (t := jump((0, 0, 0), d)) in blacks:
            blacks.remove(t)
        else:
            blacks.add(t)

    # Part 1
    print(len(blacks))

    # Part 2
    for _ in range(100):
        neighbours = Counter(jump(t, [d]) for d in ['e', 'se', 'sw', 'w', 'nw', 'ne'] for t in blacks)
        blacks = set(t for t, val in neighbours.items()
                     if val == 2 or t in blacks and val == 1)
    print(len(blacks))

    day24_1()

