#!/usr/bin/python3
""" not sail janputer """
import math

def score(fu, han, dealer):
    if ((fu == 20 or fu == 25) and han <= 1):
        return 0
    score = fu * 2 ** (han + 4) * (1 + dealer / 2)
    #score = math.ceil((math.ceil(fu / 10) * 10 if fu != 25 else 25) * 2 ** (han + 4) * (1 + dealer / 2) / 100) * 100 # pylint: disable=C0301
    if (dealer and score < 12000 or not dealer and score < 8000):
        return score
    else:
        if han <= 5:
            return 8000 + (dealer * 4000)
        elif han <= 7:
            return 12000 + (dealer * 6000)
        elif han <= 10:
            return 16000 + (dealer * 8000)
        elif han <= 12:
            return 24000 + (dealer * 12000)
        else:
            return 32000 + (dealer * 16000)

for dealer in (False, True):
    for fu in (list(range(20, 80, 2)) + [25]):
        print (fu, end = "\t")
        for han in range(1, 14):
            print (f'{int(score(fu, han, dealer)):>5}', end = "\t")
        print ("")
    print ("")
