#  Counting Duplicates
#  6 kyu
#  https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def duplicate_count(text):
    return len([c for c in set(text.lower()) if text.lower().count(c) > 1])


if __name__ == '__main__':
    basic_tests = [
        ['duplicate_count', "", 0],
        ['duplicate_count', "abcde", 0],
        ['duplicate_count', "abcdeaa", 1],
        ['duplicate_count', "abcdeaB", 2],
        ['duplicate_count', "Indivisibilities", 2]
    ]
    for test in basic_tests:
        fn_name, text, expected = test
        result = globals()[fn_name](text)
        print(f'{fn_name}("{text}") returns {result}'
              f'{f", expected: {expected}" if result != expected else ""}')


#    _               _                          _   _
#   | |             | |                        | | (_)
#   | |__   ___  ___| |_   _ __  _ __ __ _  ___| |_ _  ___ ___
#   | '_ \ / _ \/ __| __| | '_ \| '__/ _` |/ __| __| |/ __/ _ \
#   | |_) |  __/\__ \ |_  | |_) | | | (_| | (__| |_| | (_|  __/
#   |_.__/ \___||___/\__| | .__/|_|  \__,_|\___|\__|_|\___\___|
#                         | |  written by
#                         |_|  https://codewars.com/users/tpatja
'''tpatja
def duplicate_count(s):
    return len([c for c in set(s.lower()) if s.lower().count(c)>1])
'''
