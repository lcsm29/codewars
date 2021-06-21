#  One Line Task: Circle Intersection
#  2 kyu
#  https://www.codewars.com/kata/5908242330e4f567e90000a3
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
from numpy import*;circleIntersection=lambda a,b,r:r*r*(lambda c:c<1and arccos(c)-c*(1-c*c)**.5)(hypot(*subtract(b,a))/r/2)//.5


if __name__ == '__main__':
    basic_tests = [
        ['circleIntersection', [  0,   0], [  7,   0],  5,  14],
        ['circleIntersection', [  0,   0], [  0,  10], 10, 122],
        ['circleIntersection', [  5,   6], [  5,   6],  3,  28],
        ['circleIntersection', [ -5,   0], [  5,   0],  3,   0],
        ['circleIntersection', [ 10,  20], [ -5, -15], 20,  15],
        ['circleIntersection', [ -7,  13], [-25,  -5], 17, 132],
        ['circleIntersection', [-20,  -4], [-40,  29],  7,   0],
        ['circleIntersection', [ 38, -18], [ 46, -29], 10,  64],
        ['circleIntersection', [-29,  33], [ -8,  13], 15,   5],
        ['circleIntersection', [-12,  20], [ 43, -49], 23,   0],
    ]
    for test in basic_tests:
        fn_name, a, b, r, expected = test
        result = globals()[fn_name](a, b, r)
        print(f'{fn_name}({a, b, r}) returns {result}'
              f'{f", expected: {expected}" if result != expected else ""}')


#    _               _                          _   _
#   | |             | |                        | | (_)
#   | |__   ___  ___| |_   _ __  _ __ __ _  ___| |_ _  ___ ___
#   | '_ \ / _ \/ __| __| | '_ \| '__/ _` |/ __| __| |/ __/ _ \
#   | |_) |  __/\__ \ |_  | |_) | | | (_| | (__| |_| | (_|  __/
#   |_.__/ \___||___/\__| | .__/|_|  \__,_|\___|\__|_|\___\___|
#                         | |  written by
#                         |_|  https://codewars.com/users/zaz
'''zaz
from numpy import*;circleIntersection=lambda a,b,r:(lambda s:int(max(0,r*r*(s-sin(s)))))(2*arccos(hypot(*array(a)-b)/2/r))
'''
