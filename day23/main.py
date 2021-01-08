def day23_1(cups, moves, tr):
    next = [i + 1 for i in range(tr + 1)]
    for i, c in enumerate(cups[:-1],1):
        next[c] = cups[i]
        
    head = cups[0]
    if tr > len(cups):
        next[-1] = head
        next[cups[-1]] = max(cups) + 1
    else:
        next[cups[-1]] = head

    for i in range(moves):
        r = next[head]
        next[head] = next[next[next[r]]]
        allr = r, next[r], next[next[r]]

        dest = head - 1 if head > 1 else tr

        while dest in allr:
            dest = tr if dest == 1 else dest - 1

        next[next[next[r]]] = next[dest]
        next[dest] = r

        head = next[head]

    cup = next[1]
    while cup != 1:
        yield cup
        cup = next[cup]


if __name__ == '__main__':

    data = [int(i) for i in '523764819']
    r =  day23_1(data, 100, len(data))
    print(''.join(map(str,r)))
    m = day23_1(data, 10000000, 1000000)
    print(next(m) * next(m))