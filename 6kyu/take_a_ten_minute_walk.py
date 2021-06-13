#  Take a Ten Minute Walk
#  6 kyu
#  https://www.codewars.com/kata/54da539698b8a2ad76000228
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def is_valid_walk(copied):
    def get_map(minutes: int) -> list:
        base_map = [[False for _ in range(21)] for _ in range(21)]
        for i in range(10 - minutes, 11):
            for j in range(20 - i - minutes, 1 + i + minutes):
                base_map[i][j] = True
                base_map[20 - i][j] = True
        return base_map
    direc = {'n': [-1, 0], 's': [1, 0], 'e': [0, 1], 'w': [0, -1]}
    copied = walk.copy()
    pos, cp = [10, 10], copied.copy()
    for i in range(len(copied)):
        valid_map = get_map(9 - i)
        tion = copied.pop(0)
        pos[0] += direc[tion][0]
        pos[1] += direc[tion][1]
        if not valid_map[pos[0]][pos[1]]:
            return False
    return True if pos == [10, 10] and len(cp) == 10 else False


#    _               _                          _   _
#   | |             | |                        | | (_)
#   | |__   ___  ___| |_   _ __  _ __ __ _  ___| |_ _  ___ ___
#   | '_ \ / _ \/ __| __| | '_ \| '__/ _` |/ __| __| |/ __/ _ \
#   | |_) |  __/\__ \ |_  | |_) | | | (_| | (__| |_| | (_|  __/
#   |_.__/ \___||___/\__| | .__/|_|  \__,_|\___|\__|_|\___\___|
#                         | |  written by
#                         |_|  https://codewars.com/users/daddepledge
'''daddepledge
def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
'''
