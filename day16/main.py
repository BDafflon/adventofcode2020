import re
import math


def parseInput(filename):
    rules = {}
    otherTickets = []

    f = open(filename, "r")
    section = f.read().split("\n\n")

    for lines in section[0].split("\n"):
        match = re.match("(?P<name>.*): (?P<min1>\d+)-(?P<max1>\d+) or (?P<min2>\d+)-(?P<max2>\d+)", lines)
        if match:
            rules[match.group('name')] = [(int(match.group('min1')), int(match.group('max1'))), (int(match.group('min2')), int(match.group('max2')))]

    myTickets = [int(d) for d in section[1].split("\n")[1].split(",")]

    for lines in section[2].split("\n")[1:]:
        otherTickets.append([int(d) for d in lines.split(',')])

    return rules, myTickets, otherTickets



def day16_1(contrainte, otherTickets):
    return sum(t for ticket in otherTickets for t in ticket if not possible(t, contrainte))



def possible(n, rules):
    return any(min <= n <= max for value in rules.values() for min, max in value)


def check(n, rules):
    return any(min <= n <= max for min, max in rules)


def day16_2(rules, ticket, valideTicket):
    possible_ticket = [x for x in valideTicket if all(possible(y, rules) for y in x)]

    possible_fields = [{key for key, value in rules.items() if all(check(x[id_x], value) for x in possible_ticket)} for id_x in range(20)]
    
    try_possible = sorted(range(20), key=lambda x: len(possible_fields[x]))
    
    solution = [''] * 20
    for id_x in try_possible:
        if len(possible_fields[id_x]) == 1:
            solution[id_x] = tuple(possible_fields[id_x])[0]
            for i in range(20):
                if i != id_x:
                    possible_fields[i].discard(solution[id_x])
                    
    return math.prod(value for key, value in zip(solution, ticket) if "depart" in key)



if __name__ == '__main__':
    rules, myTickets, otherTickets = parseInput("input.txt")
   
    err = day16_1(rules, otherTickets)
    print(err)

    r = day16_2(rules, myTickets, otherTickets)
    print(r)