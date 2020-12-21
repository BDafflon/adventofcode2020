
def day19_1(rules,key,start, msg):

    rule = rules[key]

    if rule[0][0] in ['"a"','"b"']:
        return {start + 1} if start < len(msg) and rule[0][0][1] == msg[start] else set()
    else:
        end = set()
        end2 = set()
        for r in rule:
            buffer = {start}
            for part in r:
                b = set()
                for i in buffer:
                    b = b | day19_1(rules, part, i, msg)
                buffer = b

            print('-',end,end2,buffer,len(buffer))
            #end = end | buffer
            if len(buffer)>0:
                end2=buffer

            print('--',end,end2)
        return end2


if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    data = [l.rstrip() for l in fichier.read().split("\n\n")]

    rules = {l.split(":")[0]: [i.split(' ') for i in l.split(": ")[1].split(' | ')]  for l in data[0].split("\n")}
    data2 = [d for d in data[1].split('\n')]

    print(data2)
    r = sum([len(msg) in day19_1(rules, '0', 0, msg) for msg in data2])
    print(r)

    rules['8'] = [['42'], ['42', '8']]
    rules['11'] = [['42', '31'], ['42', '11', '31']]


    r = sum([len(msg) in day19_1(rules, '0',  0, msg) for msg in data2])
    print(r)