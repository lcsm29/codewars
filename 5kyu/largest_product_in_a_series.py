#  Largest product in a series
#  5 kyu
#  https://www.codewars.com/kata/529872bdd0f550a06b00026e
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def greatest_product(n):
    consecutives = [n[i:i + 5] for i in range(len(n) - 4)]
    ans = 0
    for con in consecutives:
        prd = 1
        for c in con:
            prd *= int(c)
        ans = max(ans, prd)
    return ans  


if __name__ == '__main__':
    basic_tests = [
        ['greatest_product', "123834539327238239583", 3_240],
        ['greatest_product', "395831238345393272382", 3_240],
        ['greatest_product', "92494737828244222221111111532909999", 5_292],
        ['greatest_product', "02494037820244202221011110532909999", 0]
    ]
    for test in basic_tests:
        fn_name, n, expected = test
        result = globals()[fn_name](n)
        print(f'{fn_name}("{n}") returns {result}'
              f'{f", expected: {expected}" if result != expected else ""}')


#    _               _                          _   _
#   | |             | |                        | | (_)
#   | |__   ___  ___| |_   _ __  _ __ __ _  ___| |_ _  ___ ___
#   | '_ \ / _ \/ __| __| | '_ \| '__/ _` |/ __| __| |/ __/ _ \
#   | |_) |  __/\__ \ |_  | |_) | | | (_| | (__| |_| | (_|  __/
#   |_.__/ \___||___/\__| | .__/|_|  \__,_|\___|\__|_|\___\___|
#                         | |  written by
#                         |_|  https://codewars.com/users/ZigiZigiBubzi
'''ZigiZigiBubzi
from itertools import islice
from functools import reduce

def greatest_product(n):
    numbers=[int(value) for value in n]
    result=[reduce(lambda x,y: x*y, islice(numbers, i, i+5), 1) for i in range(len(numbers)-4)]
    return max(result) 
'''
