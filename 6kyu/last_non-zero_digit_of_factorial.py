#  Last non-zero digit of factorial
#  6 kyu
#  https://www.codewars.com/kata/5f79b90c5acfd3003364a337
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def last_digit(n: int) -> int:
    l, a, b, c = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8], n // 5, n % 10, n // 10 % 2
    return l[n] if len(str(n)) == 1 else last_digit(a) * l[b] * 6 % 10 if c == 0 else last_digit(a) * l[b] * 4 % 10


if __name__ == '__main__':
    basic_tests = [
        ['last_digit', 3, 6],
        ['last_digit', 99, 4],
        ['last_digit', 12, 6],
        ['last_digit', 387, 2],
        ['last_digit', 1673, 4],
        ['last_digit', 10_000, 8]
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
#                         |_|  https://codewars.com/users/lechevalier
'''lechevalier
last_digit=l=lambda n,d=(1,1,2,6,4,2,2,4,2,8):n<10and d[n]or((6-n//10%10%2*2)*l(n//5)*d[n%10])%10
'''
