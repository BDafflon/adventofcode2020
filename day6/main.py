

def  day6_1(l):
    return len(list(dict.fromkeys(l)))

def day6_2(data):
    common = list(set.intersection(*map(set, [l for l in data])))
    return len(common)


if __name__ == "__main__":
    fichier = open('input.txt', 'r')
    linesDeMonFichier = [l for l in fichier.read().split('\n\n')]

    data = [ day6_1(l.replace('\n','')) for l in linesDeMonFichier ]
    print(sum(data))

    data = [day6_2(l.split('\n')) for l in linesDeMonFichier]
    print(sum(data))