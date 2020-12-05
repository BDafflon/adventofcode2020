
import itertools
import re

def byr(value):
    return 1920 <= int(value) <= 2002

def iyr(value):
    return 2010 <= int(value) <= 2020

def eyr(value):
    return 2020 <= int(value) <= 2030

def hgt(value):
    if value.endswith("cm"):
        return 150 <= int(value[0:-2]) <= 193
    else:
        if value.endswith("in"):
            return 59 <= int(value[0:-2]) <= 76
        else:
            return False

def hcl(value):
    return re.search(r'^#(?:[0-9a-fA-F]{6})$', value) is not None

def ecl(value):
    e = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return value  in e

def pid(value):
    return re.search(r'^(?:[0-9]{9})$', value) is not None

def cid(value):
    pass

def day4_2(keys,data):
    passport = [globals()[d.split(":")[0]](d.split(":")[1]) for d in data]

    return passport.count(True)

def day4_1(keys,data):
    passportKey = [ d.split(":")[0] for d in data]
    list1_as_set = set(keys)
    intersection = list1_as_set.intersection(passportKey)
    intersection_as_list = list(intersection)

    return len(intersection_as_list)


if __name__ == '__main__':
   fichier = open('input.txt', 'r')
   linesDeMonFichier = fichier.read()

   keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
   data = [  day4_2(keys ,re.split('\n| ', d)) for d in linesDeMonFichier.split('\n\n')]
   print(data.count(7))

