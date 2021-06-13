#  Multiply
#  8 kyu
#  https://www.codewars.com/kata/50654ddff44f800200000004
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def multiply(a, b):
    return a * b


if __name__ == '__main__':
    basic_tests = [
        ['multiply(1, 1)', 1, 1, 1],
        ['multiply(2, 2)', 2, 2, 4],
        ['multiply(3, 5)', 3, 5, 15],
        ['multiply(1.5, 2.5)', 1.5, 2.5, 3.75],
        ['multiply(0, 5)', 0, 5, 0],
        ['multiply(0, 0)', 0, 0, 0]
    ]
    for test in basic_tests:
        case, a, b, expected = test
        print(f'{case} returns {multiply(a, b)}{", expected: {expected}" if multiply(a, b) != expected else ""}')


#    _               _                          _   _
#   | |             | |                        | | (_)
#   | |__   ___  ___| |_   _ __  _ __ __ _  ___| |_ _  ___ ___
#   | '_ \ / _ \/ __| __| | '_ \| '__/ _` |/ __| __| |/ __/ _ \
#   | |_) |  __/\__ \ |_  | |_) | | | (_| | (__| |_| | (_|  __/
#   |_.__/ \___||___/\__| | .__/|_|  \__,_|\___|\__|_|\___\___|
#                         | |  written by
#                         |_|  https://codewars.com/users/jhoffner
'''jhoffner
def multiply(a, b):
    return a * b
'''
