#  Largest product in a series
#  5 kyu
#  https://www.codewars.com/kata/529872bdd0f550a06b00026e
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def greatest_product(n):
    consecutives = [n[i:i + 5] for i in range(len(n) - 4)]
    ans = 0
    for con in consecutives:
        prd = 1
        for c in con:
            prd *= int(c)
        ans = max(ans, prd)
    return ans  
