#  Disemvowel Trolls
#  7 kyu
#  https://www.codewars.com/kata/52fba66badcd10859f00097e
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def disemvowel(s):
    return ''.join([c for c in s if c.lower() not in 'aieou'])


if __name__ == '__main__':
    basic_tests = [
        ["disemvowel", 'This website is for losers LOL!', 'Ths wbst s fr lsrs LL!']
    ]
    for test in basic_tests:
        fn_name, s, expected = test
        result = globals()[fn_name](s)
        print(f'{fn_name}("{s}") returns "{result}"'
              f'{f", expected: {expected}" if result != expected else ""}')


#    _               _                          _   _
#   | |             | |                        | | (_)
#   | |__   ___  ___| |_   _ __  _ __ __ _  ___| |_ _  ___ ___
#   | '_ \ / _ \/ __| __| | '_ \| '__/ _` |/ __| __| |/ __/ _ \
#   | |_) |  __/\__ \ |_  | |_) | | | (_| | (__| |_| | (_|  __/
#   |_.__/ \___||___/\__| | .__/|_|  \__,_|\___|\__|_|\___\___|
#                         | |  written by
#                         |_|  https://codewars.com/users/cvk77
'''cvk77
def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")
'''
