import copy

def printData(data,swap):
    for i in range(0, len(data) ):
        for j in range(0, len(data[i]) ):
            print(data[i][j][swap],end="")
        print()


def countAdjacent(data,x,y,swap):
    seat=0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i!=x or y !=j:
                if data[i][j][swap]=='#':
                    seat+=1
    return seat

def countInView(data,x,y,swap):
    seat=0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i != x or y != j:
                diffi=i
                diffj=j
                while 1 <= diffi < len(data)-1 and 1 <= diffj < len(data[x])-1 and data[diffi][diffj][swap] == '.':
                    diffi+=i-x
                    diffj+=j-y
                if data[diffi][diffj][swap]=='#':
                    seat+=1
    return seat

def day10_1(data,gen,countfunction,maxAdjacent):
    swap=0
    for k in range(0,gen):
        modif=False
        nbSeat=0
        for i in range(1,len(data)-1):
            for j in range(1,len(data[i])-1):
                adjacent = countfunction(data,i,j,swap)
                if data[i][j][swap]=='L':
                    if adjacent==0:
                        data[i][j][(swap+1)%2]='#'
                        modif=True
                    else:
                        data[i][j][(swap + 1) % 2]=data[i][j][swap]
                elif data[i][j][swap] == '#':
                    nbSeat+=1
                    if adjacent >=maxAdjacent:
                        data[i][j][(swap + 1) % 2] = 'L'
                        modif=True
                    else:
                        data[i][j][(swap + 1) % 2] = data[i][j][swap]
                else:
                    data[i][j][(swap + 1) % 2] = data[i][j][swap]

        if not modif:
            return nbSeat
        swap = (swap+1)%2

# main
if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    linesDeMonFichier = fichier.read().splitlines()
    data = [ [['.','.']]+[[char,''] for char in i]+[['.','.']] for i in linesDeMonFichier]
    data = [[['.','.'] for char in data[0]]] + data + [[['.','.'] for char in data[0]]]

    data2=copy.deepcopy(data)

    r = day10_1(data, 100, countAdjacent, 4)
    print(r)

    r = day10_1(data2,100,countInView,5)
    print(r)
