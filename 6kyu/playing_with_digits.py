#  Playing with Digits
#  6 kyu
#  https://www.codewars.com/kata/5552101f47fc5178b1000050
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def dig_pow(n: int, p: int) -> int:
    tmp = [int(c) ** (p + i) for i, c in enumerate(str(n))]
    return sum(tmp) // n if sum(tmp) % n == 0 else -1


if __name__ == '__main__':
    basic_tests = [
        ['dig_pow', 89, 1, 1],
        ['dig_pow', 92, 1, -1],
        ['dig_pow', 46_288, 3, 51]
    ]
    for test in basic_tests:
        fn_name, n, p, expected = test
        result = globals()[fn_name](n, p)
        print(f'{fn_name}({n}, {p}) returns {result}'
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
def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1
'''
