
def day7_1(data,tag,taboo):
    bags = 0
    exploration = []
    for d in data:
        if d['bag'] not in taboo and tag in [b[1] for b in d['contain']]:
            bags+=1
            taboo.append(d['bag'])
            exploration.append(d['bag'])

    for b in exploration:
        bags += day7_1(data, b, taboo)
    return bags


def day7_2(data,tag):
    cpt = 0
    for b in [d["contain"] for d in data if d["bag"]==tag][0]:
        print(b)
        cpt += b[0] * (1 + day7_2(data,b[1]))

    return cpt

if __name__ == "__main__":
    fichier = open('input.txt', 'r')
    linesDeMonFichier = fichier.readlines()
    data = [ {'bag':d.strip().split("contain")[0].split(" bags")[0],'contain':[ [int(b[0]),b.split(" bag")[0][2:]] for b in d.strip().split("contain ")[1].split(", ") if d.strip().split("contain ")[1] != "no other bags."]}  for d in linesDeMonFichier ]
    print(day7_1(data,'shiny gold',[]))
    print(day7_2(data,'shiny gold'))