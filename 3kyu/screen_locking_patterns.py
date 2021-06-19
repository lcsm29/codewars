#  Screen Locking Patterns
#  3 kyu
#  https://www.codewars.com/kata/585894545a8a07255e0002f1
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def count_patterns_from(firstPoint, length):
    def next_pos(path):
        return [p for p in 'ABCDEFGHI'.replace(firstPoint, '') 
                if not path or p not in path and (p not in jump[path[-1]] 
                                    or jump[path[-1]][p] in path)]

    def pathfinder(limit, path=[firstPoint]):
        if limit == 0:
            return 1
        return sum([pathfinder(limit - 1, path + [p]) for p in next_pos(path)])

    paths = {
        'A': '   B  CB D  E  F  GD H  IE'.split(),
        'B': 'A     C  D  E  F  G  HE I '.split(),
        'C': 'AB B     D  E  F  GE H  IF'.split(),
        'D': 'A  B  C     E  FE G  H  I '.split(),
        'E': 'A  B  C  D     F  G  H  I '.split(),
        'F': 'A  B  C  DE E     G  H  I '.split(),
        'G': 'AD B  CE D  E  F     H  IH'.split(),
        'H': 'A  BE C  D  E  F  G     I '.split(),
        'I': 'AE B  CF D  E  F  GH H    '.split(),
    }
    jump = {k: {j[0]: j[1] for j in v if len(j) > 1} for k, v in paths.items()}
    if not 1 <= length <= 9:
        return 0
    elif 1 <= length <= 2:
        return 1 if length == 1 else len([p for p in paths[firstPoint] if len(p) == 1])
    else:
        return sum([pathfinder(length - 1)])


if __name__ == '__main__':
    basic_tests = [
        ['count_patterns_from', 'A', 10, 0],
        ['count_patterns_from', 'A', 0, 0],
        ['count_patterns_from', 'E', 14, 0],
        ['count_patterns_from', 'B', 1, 1],
        ['count_patterns_from', 'C', 2, 5],
        ['count_patterns_from', 'E', 2, 8],
        ['count_patterns_from', 'E', 4, 256]
    ]
    for test in basic_tests:
        fn_name, first_point, length, expected = test
        result = globals()[fn_name](first_point, length)
        print(f'{fn_name}({first_point, length}) returns {result}'
              f'{f", expected: {expected}" if result != expected else ""}')


#    _               _                          _   _
#   | |             | |                        | | (_)
#   | |__   ___  ___| |_   _ __  _ __ __ _  ___| |_ _  ___ ___
#   | '_ \ / _ \/ __| __| | '_ \| '__/ _` |/ __| __| |/ __/ _ \
#   | |_) |  __/\__ \ |_  | |_) | | | (_| | (__| |_| | (_|  __/
#   |_.__/ \___||___/\__| | .__/|_|  \__,_|\___|\__|_|\___\___|
#                         | |  written by
#                         |_|  https://codewars.com/users/Blind4Basics
'''Blind4Basics
EQUIV_PTS = {same: src for src,seq in (('A','CGI'), ('B','DFH')) for same in seq}

ALL       =  set('ABCDEFGHI')
LINKED_TO = {'A': ('BC','DG','EI','F', 'H'),
             'B': ('A', 'C', 'D', 'EH','F', 'G', 'I'),
             'C': ('BA','D', 'EG','FI','H'),
             'D': ('A', 'B', 'C', 'EF','G', 'H', 'I'),
             'E': tuple('ABCDFGHI'),
             'F': ('A', 'B', 'C', 'ED','G', 'H', 'I'),
             'G': ('DA','B', 'EC','F', 'HI'),
             'H': ('A', 'EB','C', 'D', 'F', 'G', 'I'),
             'I': ('EA','B', 'FC','D', 'HG')
            }


def DFS(c, depth, root, seens, patterns):
    if depth > len(ALL): return                
    
    patterns[root][depth] += 1
    
    seens.add(c)
    toExplore = ''.join( next((n for n in seq if n not in seens), '') for seq in LINKED_TO[c] )
    for nextC in toExplore:
        DFS(nextC, depth+1, root, seens, patterns)
    seens.discard(c)
    

PATTERNS = {}
for c in "ABE":
    PATTERNS[c] = [0]*10
    DFS(c, 1, c, set(), PATTERNS)


def count_patterns_from(start, length):
    if not (0 < length < 10) or start not in ALL: return 0    
    
    actualStart = EQUIV_PTS.get(start, start)
    return PATTERNS[actualStart][length]
'''
