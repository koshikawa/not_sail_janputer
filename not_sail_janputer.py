#!/usr/bin/python3
""" not sail janputer """
import math

def get_score(fu, han, dealer):
    """ 得点を返す """
    if (fu in (20, 25) and han <= 1):
        return 0
    child_score = min(fu * 2 ** (han + 4), 8000)
    if han in (6, 7):
        child_score = 12000
    if han in (8, 9, 10):
        child_score = 16000
    if han in (11, 12):
        child_score = 24000
    if han >= 13:
        child_score = 32000

    return child_score * (1 + dealer * 0.5)

for dealer in (False, True):
    for fu in (list(range(20, 80, 2)) + [25]):
        print (fu, end = "\t")
        for han in range(1, 14):
            print (f'{int(get_score(fu, han, dealer)):>5}', end = "\t")
        print ("")
    print ("")
