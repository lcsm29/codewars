#  parseInt() reloaded
#  4 kyu
#  https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def parse_int(string: str) -> int:
    d = {word: number for number, word in enumerate('''
        zero one two three four five six seven eight nine
        ten eleven twelve thirteen fourteen fifteen
        sixteen seventeen eighteen nineteen'''.split())}
    d.update({word: number for number, word in zip(range(20, 101, 10),
        'twenty thirty forty fifty sixty seventy eighty ninety hundred'.split())})
    a = []
    for s in string.split('thousand'):
        total = 0
        for i in s.strip().split():
            if '-' in i:
                for j in i.split('-'):
                    total += d.get(j)
            else:
                if i in d:
                    total = total * d.get(i) if 'hund' in i else total + d.get(i)
        a.append(total)
    return 1000000 if 'million' in string else a[0] * 1000 + a[1] if len(a) > 1 else a[0]


if __name__ == '__main__':
    basic_tests = [
        ['parse_int', "one", 1],
        ['parse_int', "twenty", 20],
        ['parse_int', "two hundred forty-six", 246]
    ]
    for test in basic_tests:
        fn_name, string, expected = test
        result = globals()[fn_name](string)
        print(f'{fn_name}("{string}") returns {result}'
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
words = {w: n for n, w in enumerate('zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split())}
words.update({w: 10 * n for n, w in enumerate('twenty thirty forty fifty sixty seventy eighty ninety hundred'.split(), 2)})
thousands = {w: 1000 ** n for n, w in enumerate('thousand million billion trillion quadrillion quintillion sextillion septillion octillion nonillion decillion'.split(), 1)}
def parse_int(strng):
    num = group = 0
    for w in strng.replace(' and ', ' ').replace('-', ' ').split():
        if w == 'hundred': group *= words[w]
        elif w in words: group += words[w]
        else:
            num += group * thousands[w]
            group = 0
    return num + group
'''
