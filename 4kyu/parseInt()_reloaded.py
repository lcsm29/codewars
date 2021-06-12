#  parseInt() reloaded
#  4 kyu
#  https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def parse_int(string):
    d = {word: number for number, word in enumerate('''
        zero one two three four five six seven eight nine
        ten eleven twelve thirteen fourteen fifteen
        sixteen seventeen eighteen nineteen'''.split())}
    d.update({word: number for number, word in zip(range(20, 101, 10),
        'twenty thirty forty fifty sixty seventy eighty ninety hundred'.split())})
    a = []
    for s in string.split('thousand'):
        total = 0
        for i in s.strip().split():
            if '-' in i:
                for j in i.split('-'):
                    total += d.get(j)
            else:
                if i in d:
                    total = total * d.get(i) if 'hund' in i else total + d.get(i)
        a.append(total)
    return 1000000 if 'million' in string else a[0] * 1000 + a[1] if len(a) > 1 else a[0]
