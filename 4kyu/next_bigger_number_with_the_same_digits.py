#  Next bigger number with the same digits
#  4 kyu
#  https://www.codewars.com/kata/55983863da40caa2c900004e
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def next_bigger(n):
    n = list(str(n))
    try:
        k = max(i for i in range(1, len(n)) if n[i - 1] < n[i])
        l = max(j for j in range(k, len(n)) if n[j] > n[k - 1])
    except:
        return -1
    n[l], n[k - 1] = n[k - 1], n[l]
    n[k:] = reversed(n[k:])
    return int(''.join([str(i) for i in n]))
