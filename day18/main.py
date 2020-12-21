import copy
import re



def day18_2(data):
    regexRec = re.search(r"(\((\d+)(\s([+*])\s(\d+))+\))", data)
    if regexRec:
        return day18_2(data.replace(regexRec.groups()[0], str(day18_2(regexRec.groups()[0][1:-1])), 1))
    else:
        regexOP = re.search(r"(\d+)\s\+\s(\d+)", data)
        if regexOP:
            return day18_2(
                data.replace(regexOP.group(), str(int(regexOP.groups()[0]) + int(regexOP.groups()[1])), 1))
        else:
            regexOP = re.search(r"(\d+)\s\*\s(\d+)", data)
            if regexOP:
                return day18_2(
                    data.replace(regexOP.group(), str(int(regexOP.groups()[0]) * int(regexOP.groups()[1])), 1))
    return int(data)



def day18_1(data):
    regexRec = re.search(r"(\((\d+)(\s([+*])\s(\d+))+\))", data)
    if regexRec:
        return day18_1(data.replace(regexRec.groups()[0], str(day18_1(regexRec.groups()[0][1:-1])), 1))
    else:
        regexOP = re.match(r"(\d+)\s([+*])\s(\d+)", data)
        if regexOP:
            nb1, op, nb2 = regexOP.groups()
            return day18_1(
                data.replace(regexOP.group(), str(int(nb1) + int(nb2) if op == "+" else int(nb1) * int(nb2)), 1))
    return int(data)


if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    data = fichier.read().splitlines()
    data2 = copy.deepcopy(data)

    r = sum([day18_1(d) for d in data])
    print(r)


    r = sum([day18_2(d) for d in data2])
    print(r)
