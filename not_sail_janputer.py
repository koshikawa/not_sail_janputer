#!/usr/bin/python3
"""
not sail janputer 
切り上げしない1翻から13翻までの点数を計算する
"""


def over_mangan(h):
    """満貫以上の場合の点数を返す"""
    if 4 <= h <= 13:
        return ((h // 2) * 4000 - minus9plus(h) * 4000) * 2 ** (minus9plus(h) // 2)
    else:
        return 8000


def minus9plus(input_number):
    """9を引いた正の値を返す"""
    return max(0, input_number - 9)


def get_score(f, h, d):
    """得点を返す"""
    if f in (20, 25) and h <= 1:
        return 0
    return min(f * 2 ** (h + 4), over_mangan(h)) * (1 + d * 0.5)


for dealer in (False, True):
    for fu in list(range(20, 80, 2)) + [25]:
        print(fu, end="\t")
        for han in range(1, 14):
            print(f"{int(get_score(fu, han, dealer)):>5}", end="\t")
        print("")
    print("")
