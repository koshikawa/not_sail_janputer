#!/usr/bin/python3
""" not sail janputer """
import math

def get_score(fu, han, dealer):
    """ 得点を返す """
    child_score = fu * 2 ** (han + 4)

    if ((fu == 20 or fu == 25) and han <= 1):
        return 0
    if child_score >= 8000:
        child_score = 8000
    if han >= 6:
        child_score = 12000
    if han >= 8:
        child_score = 16000
    if han >= 11:
        child_score = 24000
    if han >= 13:
        child_score = 32000

    return child_score + (child_score * dealer * 0.5)

for dealer in (False, True):
    for fu in (list(range(20, 80, 2)) + [25]):
        print (fu, end = "\t")
        for han in range(1, 14):
            print (f'{int(get_score(fu, han, dealer)):>5}', end = "\t")
        print ("")
    print ("")
