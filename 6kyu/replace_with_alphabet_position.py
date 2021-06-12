#  Replace With Alphabet Position
#  6 kyu
#  https://www.codewars.com/kata/546f922b54af40e1e90001da
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
from string import punctuation as p, ascii_lowercase as lo


def alphabet_position(text):
    d = {c: i+1 for i, c in enumerate(lo)}
    return ' '.join([str(d[c.lower()]) for w in text.split() for c in w.strip(p) if c.encode().isalpha()])
