def day3_2(data, slope):
    cpt=1
    for i in slope:
        cpt*=day3_1(data,i[0],i[1])
    return cpt

def day3_1(data,right,down):
    cpt=0
    i=0
    j=0
    while i < len(data):

        if data[i][j] == '#':
            cpt += 1
        j+=right

        if j >= len(data[i]):
            j -= len(data[i])

        i += down

    return cpt

# main
if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    linesDeMonFichier = fichier.readlines()
    data = []

    for i in linesDeMonFichier:
        data = data + [list(i)[0:len(i)-1]]

    tree = day3_2(data,[[1,1],[3,1],[5,1],[7,1],[1,2]])
    print(tree)