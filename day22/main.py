import regex


def day22_2_rec(p1,p2):
    seen = set()
    while p1 and p2:
        tuple1 = tuple(p1)
        tuple2 = tuple(p2)
        
        if (tuple1, tuple2) in seen:
            return p1, []
        seen.add((tuple1, tuple2))

        card_1 = p1.pop(0)
        card_2 = p2.pop(0)

        if len(p1) >= card_1 and len(p2) >= card_2:
            subp1, subp2 = day22_2_rec(p1[:card_1], p2[:card_2])
            player1Wins = len(subp1) > 0
        else:
            player1Wins = card_1 > card_2

        if player1Wins:
            p1 += [card_1, card_2]
        else:
            p2 += [card_2, card_1]

    return p1,p2

def day22_2(p1,p2):
    p1,p2 = day22_2_rec(p1,p2)

    winner = p1 or p2

    total = 0
    winner.reverse()
    for m, c in enumerate(winner):
        total += (m + 1) * c
    return total

def day22_1(p1,p2):

    while p1 and p2:
        card_1 = p1.pop(0)
        card_2 = p2.pop(0)

        if card_1 > card_2:
            p1+=[card_1, card_2]
        elif card_2 > card_1:
            p2+=[card_2, card_1]

    winner = p1 or p2


    total = 0
    winner.reverse()
    for m, c in enumerate(winner):
        total += (m + 1) * c
    return total


if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    data = fichier.read().split('\n\n')

    player_1 = [int(d) for d in data[0].split(':')[1].split()]
    player_2 = [int(d) for d in data[1].split(':')[1].split()]

    print(day22_1(player_1,player_2))


    player_1 = [int(d) for d in data[0].split(':')[1].split()]
    player_2 = [int(d) for d in data[1].split(':')[1].split()]
    print(player_1, player_2)
    print(day22_2(player_1, player_2))
