#  Descending Order
#  7 kyu
#  https://www.codewars.com/kata/5467e4d82edf8bbf40000155
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def descending_order(n):
    d = {str(i): 0 for i in range(10)}
    for i in str(n):
        d[i] += 1
    return int(''.join([k * v for k, v in reversed(d.items())]))
