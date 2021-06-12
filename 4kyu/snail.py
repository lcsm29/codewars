#  Snail
#  4 kyu
#  https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def snail(a):
    pos, start, limit = [], 0, len(a) - 1
    while limit:
        r = [[start, i] for i in range(start, limit)]
        d = [[i, limit] for i in range(start, limit)]
        l = [[limit, i] for i in range(limit, start, -1)]
        u = [[i, start] for i in range(limit, start, -1)]
        for l in r + d + l + u:
            pos.append([l[0], l[1]])
        start, limit = start + 1, limit - 1
        if start == limit:
            pos.append([start, limit])
    return [a[p[0]][p[1]] for p in pos] if len(pos) != 0 else a[0] if type(a[0]) == list else a
