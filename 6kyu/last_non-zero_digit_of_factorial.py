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
def last_digit(n):
    l, a, b, c = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8], n // 5, n % 10, n // 10 % 2
    return l[n] if len(str(n)) == 1 else last_digit(a) * l[b] * 6 % 10 if c == 0 else last_digit(a) * l[b] * 4 % 10
