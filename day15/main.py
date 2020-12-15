import time


def day15_1(data,limit):
    dic = { d:[i,i] for i,d in enumerate(data)}
    last = data[len(data)-1]

    for i in range (len(data),limit):
        nb = dic[last][1] - dic[last][0]
        if nb in dic.keys():
            dic[nb] = [dic[nb][1], i]
        else:
            dic[nb] = [i, i]
        last = nb
    return last


if __name__ == '__main__':
    l=[14,8,16,0,1,17]

    tic = time.perf_counter()
    r = day15_1(l, 30000000)
    toc = time.perf_counter()

    print(toc - tic," : ",r)