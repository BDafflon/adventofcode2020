
def check_number(data,n):
    for i in range(0,len(data)):
        for j in range(i,len(data)):
            if n == data[i]+data[j]:
                return True
    return False

def day9_1(data):
    buffer = 25
    subData = data[0:buffer]

    for i in data[buffer:]:
        if not check_number(subData,i):
            return i
        subData.pop(0)
        subData.append(i)
    return None

def day9_2_process(data,n):
    for i in range(0,len(data)):
        sum = n
        for j in range(i,len(data)):
            sum-=data[j]
            if sum == 0:
                return i,j
            if sum < 0:
                break
    return None, None

def day9_2(data,n):
    i,j = day9_2_process(data,n)
    if i is not None:
        return max(data[i:j])+min(data[i:j])
    return -1

if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    lignes = fichier.read().splitlines()
    data = [int(i) for i in lignes]
    res = day9_1(data)
    print(res)

    res = day9_2(data,res)
    print(res)