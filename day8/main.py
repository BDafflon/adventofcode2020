import copy
import time

def acc(value,i,accu):
    return accu+value,i+1

def jmp(value,i,accu):
    return accu,i+value

def nop(value,i,accu):
    return accu,i+1


def day8_1(data,i,accu):
    if data[i][2]==1:
        return accu
    else :
        data[i][2]+=1
        accu,i=globals()[data[i][0]](data[i][1],i,accu)
        return day8_1(data,i,accu)

def day8_2_process(data,i,accu):
    if len(data)<=i:
        return accu
    else :
        if data[i][2] == 2:
            return None
        else :
            data[i][2]+=1
            accu,i=globals()[data[i][0]](data[i][1],i,accu)
            return day8_2_process(data,i,accu)

def swap(data,i):

    swapNotDone = True

    while swapNotDone:
        if data[i][2]==1:
            if data[i][0]=='jmp':
                data[i][0]='nop'
                return i+1
            if data[i][0]=='nop':
                data[i][0]='jmp'
                return i+1
        i+=1
    return -1

def day8_2(data,i):
    dataBackup = copy.deepcopy(data)
    lastSwap = 0
    lastSwap = swap(data,lastSwap)

    while lastSwap != -1:
        accu = day8_2_process(data,0,0)
        if accu is None:
            data = copy.deepcopy(dataBackup)
            lastSwap = swap(data, lastSwap)
        else:
            return accu
    return None



# main
if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    linesDeMonFichier = fichier.read().splitlines()


    data = [ [i.split(" ")[0],int(i.split(" ")[1]),0] for i in linesDeMonFichier]


    accu = day8_1(data,0,0)
    print('part1 :',accu)

    tic = time.perf_counter()
    print('part2 :',day8_2(data,0))
    toc = time.perf_counter()
    print("time ",toc-tic)




