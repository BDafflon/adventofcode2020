

def day10_2(data,buit_in):
    #https://math.stackexchange.com/questions/284700/maximum-number-of-path-for-acyclic-graph-with-start-and-end-node
    path = [[j, 0] for j in data]
    path.append([buit_in, 1])

    for j in range(len(path) - 2, -1, -1):
        s = sum([x[1] for x in path if 0 <= x[0] - path[j][0] <= 3])
        path[j][1] = s

    return path[0][1]

def day10_1(data,built_in):
    diff=[]
    for i in range(0,len(data)-1):
        diff.append(data[i+1]-data[i])
    diff.append(built_in - data[len(data)-1])
    return  diff.count(1)* diff.count(3)

if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    lignes = fichier.read().splitlines()

    data =  [0]+[int(i) for i in lignes]
    data.sort()
    print(data)
    built_in = data[len(data)-1]+3

    print(day10_1(data,built_in))
    print(day10_2(data,built_in))
