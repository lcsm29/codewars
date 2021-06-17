#  Next bigger number with the same digits
#  4 kyu
#  https://www.codewars.com/kata/55983863da40caa2c900004e
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def next_bigger(n: int) -> int:
    n = list(str(n))
    try:
        k = max(i for i in range(1, len(n)) if n[i - 1] < n[i])
        l = max(j for j in range(k, len(n)) if n[j] > n[k - 1])
    except:
        return -1
    n[l], n[k - 1] = n[k - 1], n[l]
    n[k:] = reversed(n[k:])
    return int(''.join([str(i) for i in n]))


if __name__ == '__main__':
    basic_tests = [
        ['next_bigger', 12, 21],
        ['next_bigger', 513, 531],
        ['next_bigger', 2017, 2071],
        ['next_bigger', 414, 441],
        ['next_bigger', 144, 414]
    ]
    for test in basic_tests:
        fn_name, n, expected = test
        result = globals()[fn_name](n)
        print(f'{fn_name}({n}) returns {result}'
              f'{f", expected: {expected}" if result != expected else ""}')


#    _               _                          _   _
#   | |             | |                        | | (_)
#   | |__   ___  ___| |_   _ __  _ __ __ _  ___| |_ _  ___ ___
#   | '_ \ / _ \/ __| __| | '_ \| '__/ _` |/ __| __| |/ __/ _ \
#   | |_) |  __/\__ \ |_  | |_) | | | (_| | (__| |_| | (_|  __/
#   |_.__/ \___||___/\__| | .__/|_|  \__,_|\___|\__|_|\___\___|
#                         | |  written by
#                         |_|  https://codewars.com/users/zed9h
'''zed9h
import itertools
def next_bigger(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i] < s[i+1]:
            t = s[i:]
            m = min(filter(lambda x: x>t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1
'''
