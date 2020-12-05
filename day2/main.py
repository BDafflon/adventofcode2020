import re
import time

current_milli_time = lambda: int(round(time.time() * 1000))

def day2(data,part):
    passwordValid=0
    for d in data:
        if part == 1:
            if d['mini']<= sum(map(lambda x : 1 if d['letter'] in x else 0, d['pwd'])) <= d['maxi']  :
                passwordValid += 1
        else :
            if (d['pwd'][d['mini']-1]==d['letter'] and d['pwd'][d['maxi']-1]!=d['letter']) or (d['pwd'][d['mini']-1]!=d['letter'] and d['pwd'][d['maxi']-1]==d['letter']):
                passwordValid+=1
    return passwordValid


if __name__ == '__main__':
    start = current_milli_time()

    file1 = open('in.py', 'r')
    Lines = file1.readlines()
    file1.close()
    data = []

    for l in Lines:
        resplit = re.split("(\d+)-(\d+) (\w): (.+)", l)

        if len(resplit) >= 4:
            mini = int(resplit[1])
            maxi = int(resplit[2])
            letter = resplit[3]
            pwd = resplit[4]

            data.append({'mini':mini,'maxi':maxi,"letter":letter, "pwd":pwd})

    resultat=day2(data,2)
    print(resultat)
    end = current_milli_time() - start
    print(end)

