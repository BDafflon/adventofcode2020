
def day5_1(mini,maxi,data):
    if data=='':
        return [mini,maxi]
    else:
        if data[0]=='F' or data[0]=='L':
            return day5_1(mini,mini+int((maxi-mini)/2),data[1:])
        else:
            return day5_1(mini+int((maxi-mini)/2)+1,maxi,data[1:])

def day5_2(data):
    fulliD = [i for i in range(data[0],data[len(data)-1])]

    return set(fulliD) - set(data)


# main
if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    linesDeMonFichier = fichier.read()

    data = [day5_1(0,127,d[:-3])[0]*8+day5_1(0,7,d[-3:])[1] for d in linesDeMonFichier.split('\n')]
    data.sort()
    id = day5_2(data)
    print(id)

