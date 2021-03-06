#  Categorize New Member
#  7 kyu
#  https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def open_or_senior(data: list[tuple[int]]) -> list[str]:
    return ['Senior' if l[0] >= 55 and l[1] > 7 else 'Open' for l in data]


if __name__ == '__main__':
    basic_tests = [
        ["open_or_senior", [(45, 12),(55,21),(19, -2),(104, 20)], ['Open', 'Senior', 'Open', 'Senior']],
        ["open_or_senior", [(16, 23),(73,1),(56, 20),(1, -1)], ['Open', 'Open', 'Senior', 'Open']]
    ]
    for test in basic_tests:
        fn_name, data, expected = test
        result = globals()[fn_name](data)
        print(f'{fn_name}({data}) returns {result}'
              f'{f", expected: {expected}" if result != expected else ""}')


#    _               _                          _   _
#   | |             | |                        | | (_)
#   | |__   ___  ___| |_   _ __  _ __ __ _  ___| |_ _  ___ ___
#   | '_ \ / _ \/ __| __| | '_ \| '__/ _` |/ __| __| |/ __/ _ \
#   | |_) |  __/\__ \ |_  | |_) | | | (_| | (__| |_| | (_|  __/
#   |_.__/ \___||___/\__| | .__/|_|  \__,_|\___|\__|_|\___\___|
#                         | |  written by
#                         |_|  https://codewars.com/users/taw
'''taw
def openOrSenior(data):
    return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]
'''
