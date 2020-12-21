import copy
def day14_2_combinaison(nbBin):
    allCombinaisons = [nbBin]
    for i, c in enumerate(nbBin):
        if c != 'X':
            for combinaison in allCombinaisons:
                combinaison[i] = c
        else:
            newCombinaisons = []
            for combinaison in allCombinaisons:
                combinaison[i] = '1'
                newCombinaisons.append(combinaison[:])
                combinaison[i] = '0'
                newCombinaisons.append(combinaison[:])
            allCombinaisons = copy.deepcopy(newCombinaisons)
    return [ ''.join(map(str, c)) for c in allCombinaisons]


def day14_2(data):
    registre = {}
    for d in data:
        for n in d[1]:
            nBin = '{:036b}'.format(n[0])
            nBin = ['0' if i >= len(nBin) else nBin[i] if mask_bit == '0' else mask_bit for i, mask_bit in enumerate(d[0])]
            combinaisons = day14_2_combinaison(nBin)
            for c in combinaisons:
                registre[int(c, 2)] = n[1]
    return sum(registre.values())




def day14_1(data):
    registre = {}
    for d in data:
        for n in d[1]:
            nBin = '{:036b}'.format(n[1])
            registre[n[0]] = int(''.join([('0' if i >= len(nBin) else nBin[i]) if mask_bit == 'X' else mask_bit for i, mask_bit in enumerate(d[0])]), 2)

    return sum(registre.values())


# main
if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    linesDeMonFichier = fichier.read().replace(' ', ' ').split("mask = ")[1:]

    data = [[d.replace('\n', ' ').split(" ")[0]] + [[[int(f) for f in e.replace("mem[", '').split('] = ')] for e in
                                                     d[len(d.replace('\n', ' ').split(" ")[0]) + 1:].split('\n') if
                                                     e != '']] for d in linesDeMonFichier]

    res = day14_1(data)
    print(res)
    res=day14_2(data)
    print(res)
