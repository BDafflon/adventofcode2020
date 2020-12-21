from math import sqrt
import numpy as np

class Map(object):
    def __init__(self, inp_str):
        self.tilesList = [Tile(int(ln[5:9]), ln.split('\n')[1:]) for ln in inp_str]
        self.width = int(sqrt(len(self.tilesList)))
        self.grid = [[[] for i in range(self.width)] for n in range(self.width)]
        self.pair()

    def pair(self):
        for tile in self.tilesList:
            for other in self.tilesList:
                tile.pair(other)

    def edges(self):
        return [t.id for t in self.tilesList if t.link() == 2]


class Tile(object):
    def __init__(self, id, lines):
        self.id = id
        self.lines = lines
        self.borders = [lines[0], lines[-1], ''.join([i[0] for i in lines]),
                      ''.join([i[-1] for i in lines])]
        self.flpd = [i[::-1] for i in self.borders]
        self.pairs = []

    def pair(self, other):
        if self.id != other.id:
            for side, border in enumerate(other.borders):
                if border in self.borders or border in self.flpd:
                    self.pairs.append(other.id)

    def trim(self):
        self.lines = [ln[1:-1] for ln in self.lines[1:-1]]


    def link(self):
        return len(self.pairs)




def day20_1(map):
    acum = 1
    for t in map.edges():
        acum *= t
    return acum

def day20_2(map):
    monster_str = (
        "                  # \n"
        "#    ##    ##    ###\n"
        " #  #  #  #  #  #   ".splitlines()
    )

    monster = np.array([[c == "#" for c in l] for l in monster_str], dtype=np.uint8)

    for image in map:
        count = 0
        for i in range(image.shape[0] - monster.shape[0] + 1):
            for j in range(image.shape[1] - monster.shape[1] + 1):
                check = image[i: i + monster.shape[0], j: j + monster.shape[1]]
                if (check & monster == monster).all():
                    count += 1
        if count:
            break
    return int(np.sum(image) - count * np.sum(monster))

if __name__ == '__main__':
    fichier = open('input.txt', 'r')

    map = Map(fichier.read().split('\n\n'))
    print(day20_1(map))
    print(day20_2(map))
    