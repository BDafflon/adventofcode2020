import math

def day13_1(data,target):
    l = [ ( ((target//d)+1)*d) - target for d in data]
    return data[l.index(min(l))],min(l)

def day13_2(data):
    _, deps = zip(*data)
    trouver = 1
    depart = data[0][0] + data[0][1]
    increment = math.prod(deps[:trouver])

    while True:
        if all([(depart + t_plus) % bus_id == 0 for t_plus, bus_id in data[:trouver + 1]]):
            trouver += 1
            increment = math.prod(deps[:trouver])
            if trouver == len(deps):
                return depart
        depart += increment
    print(depart)


 # main
if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    linesDeMonFichier = fichier.read().splitlines()
    target = int(linesDeMonFichier[0])
    print(target)
    bus = [ int(d)  for d in linesDeMonFichier[1].split(',') if d !='x']
    print(bus)
    id,minute = day13_1(bus,target)
    print(id * minute)

    data = [(t, int(d)) for t, d in enumerate(linesDeMonFichier[1].split(',')) if d != 'x']
    print(day13_2(data))
