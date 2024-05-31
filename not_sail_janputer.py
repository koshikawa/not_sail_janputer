#!/usr/bin/python3
"""
not sail janputer 
切り上げしない1翻から13翻までの点数を計算する
"""


def minus9plus(input_number):
    """9を引いた正の値を返す"""
    return max(0, input_number - 9)


def get_score(f, h, d):
    """得点を返す"""
    return (
        min(
            f * 2 ** (h + 4),
            (
                ((h // 2) * 4000 - minus9plus(h) * 4000) * 2 ** (minus9plus(h) // 2)
                if 4 <= h
                else 8000
            ),
        )
        * (1 + d * 0.5)
        if not (f in (20, 25) and h <= 1)
        else 0
    )


for dealer in (False, True):
    for fu in list(range(20, 80, 2)) + [25]:
        print(fu, end="\t")
        for han in range(1, 14):
            print(f"{int(get_score(fu, han, dealer)):>5}", end="\t")
        print("")
    print("")
