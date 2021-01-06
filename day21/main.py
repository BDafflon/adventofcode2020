import regex


def day21_2(find):
    return ','.join([val for key, val in sorted(find.items())])


def day21_1(possible, ingredients):
    find = {}
    while possible:
        for a, i in list(possible.items()):
            if len(i) == 1:
                find[a] = list(i)[0]
                possible.pop(a)
            else:
                possible[a] -= set(find.values())
    return len([ingredient for ingredient in ingredients if ingredient not in find.values()]), find


if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    lignes = fichier.read().split('\n')
    possible = {}
    ingredients = []
    for data in lignes:
        re = regex.search(r'(?:(?P<listI>\w+)(?: )?)+\(contains (?:(?P<listA>\w+)(?:, )?)+\)', data).capturesdict()
        ingredients+=re['listI']
        for al in re['listA']:
            if al in possible:
                possible[al]=possible[al].intersection(set(re['listI']))
            else:
                possible[al] = set(re['listI'])

    r, find = day21_1(possible, ingredients)
    print(r)
    r = day21_2(find)
    print(r)
