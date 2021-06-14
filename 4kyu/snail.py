#  Snail
#  4 kyu
#  https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def snail(a):
    pos, start, limit = [], 0, len(a) - 1
    while limit:
        r = [[start, i] for i in range(start, limit)]
        d = [[i, limit] for i in range(start, limit)]
        l = [[limit, i] for i in range(limit, start, -1)]
        u = [[i, start] for i in range(limit, start, -1)]
        for position in r + d + l + u:
            pos.append([position[0], position[1]])
        start, limit = start + 1, limit - 1
        if start == limit:
            pos.append([start, limit])
    return [a[p[0]][p[1]] for p in pos] if len(pos) != 0 else a[0] if type(a[0]) == list else a


if __name__ == '__main__':
    basic_tests = [
        ['snail', [[1,2,3],
                   [4,5,6],
                   [7,8,9]],
            [1,2,3,6,9,8,7,4,5]
        ],
        ['snail', [[1,2,3],
                   [8,9,4],
                   [7,6,5]],
            [1,2,3,4,5,6,7,8,9]
        ]
    ]
    for test in basic_tests:
        fn_name, a, expected = test
        result = globals()[fn_name](a)
        print(f'{fn_name}({a}) returns {result}'
              f'{f", expected: {expected}" if result != expected else ""}')


#    _               _                          _   _
#   | |             | |                        | | (_)
#   | |__   ___  ___| |_   _ __  _ __ __ _  ___| |_ _  ___ ___
#   | '_ \ / _ \/ __| __| | '_ \| '__/ _` |/ __| __| |/ __/ _ \
#   | |_) |  __/\__ \ |_  | |_) | | | (_| | (__| |_| | (_|  __/
#   |_.__/ \___||___/\__| | .__/|_|  \__,_|\___|\__|_|\___\___|
#                         | |  written by
#                         |_|  https://codewars.com/users/jolaf
'''jolaf
def snail(array):
    ret = []
    if array and array[0]:
        size = len(array)
        for n in xrange((size + 1) // 2):
            for x in xrange(n, size - n):
                ret.append(array[n][x])
            for y in xrange(1 + n, size - n):
                ret.append(array[y][-1 - n])
            for x in xrange(2 + n, size - n + 1):
                ret.append(array[-1 - n][-x])
            for y in xrange(2 + n, size - n):
                ret.append(array[-y][n])
    return ret
'''
