#  Sort binary tree by levels
#  4 kyu
#  https://www.codewars.com/kata/52bef5e3588c56132c0003bc
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def tree_by_levels(node):
    if not node:
        return []
    else:
        answer, queue = [], [node]
        while queue:
            tmp = node.pop(0)
            if tmp is not None:
                answer.append(tmp.value)
                queue += [tmp.left, tmp.right]
        return answer
