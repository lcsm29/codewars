#  Sum of Intervals
#  4 kyu
#  https://www.codewars.com/kata/52b7ed099cdc285c300001cd
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def sum_of_intervals(intervals: list[tuple[int]]) -> int:
    return len(set([i for a, b in intervals for i in range(a, b)]))


if __name__ == '__main__':
    basic_tests = [
        ['sum_of_intervals', [(1, 5)], 4],
        ['sum_of_intervals', [(1, 5), (6, 10)], 8],
        ['sum_of_intervals', [(1, 5), (1, 5)], 4],
        ['sum_of_intervals', [(1, 4), (7, 10), (3, 5)], 7]
    ]
    for test in basic_tests:
        fn_name, intervals, expected = test
        result = globals()[fn_name](intervals)
        print(f'{fn_name}({intervals}) returns {result}'
              f'{f", expected: {expected}" if result != expected else ""}')


#    _               _                          _   _
#   | |             | |                        | | (_)
#   | |__   ___  ___| |_   _ __  _ __ __ _  ___| |_ _  ___ ___
#   | '_ \ / _ \/ __| __| | '_ \| '__/ _` |/ __| __| |/ __/ _ \
#   | |_) |  __/\__ \ |_  | |_) | | | (_| | (__| |_| | (_|  __/
#   |_.__/ \___||___/\__| | .__/|_|  \__,_|\___|\__|_|\___\___|
#                         | |  written by
#                         |_|  https://codewars.com/users/Hunter_71
'''Hunter_71
def sum_of_intervals(intervals):
    result = set()
    for start, stop in intervals:
        for x in range(start, stop):
            result.add(x)
            
    return len(result)
'''
