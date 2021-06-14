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
            tmp = queue.pop(0)
            if tmp is not None:
                answer.append(tmp.value)
                queue += [tmp.left, tmp.right]
        return answer


if __name__ == '__main__':
    class Node:
        def __init__(self, L, R, n):
            self.left = L
            self.right = R
            self.value = n
    basic_tests = [
        ['tree_by_levels', None, [], 'None'],
        ['tree_by_levels', Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1), [1, 2, 3, 4, 5, 6], 'Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)']
    ]
    for test in basic_tests:
        fn_name, node, expected, str_node = test
        result = globals()[fn_name](node)
        print(f'{fn_name}({str_node}) returns {result}'
              f'{f", expected: {expected}" if result != expected else ""}')


#    _               _                          _   _
#   | |             | |                        | | (_)
#   | |__   ___  ___| |_   _ __  _ __ __ _  ___| |_ _  ___ ___
#   | '_ \ / _ \/ __| __| | '_ \| '__/ _` |/ __| __| |/ __/ _ \
#   | |_) |  __/\__ \ |_  | |_) | | | (_| | (__| |_| | (_|  __/
#   |_.__/ \___||___/\__| | .__/|_|  \__,_|\___|\__|_|\___\___|
#                         | |  written by
#                         |_|  https://codewars.com/users/suic
'''suic
from collections import deque


def tree_by_levels(node):
    if not node:
        return []
    res, queue = [], deque([node,])
    while queue:
        n = queue.popleft()
        res.append(n.value)
        if n.left is not None:
            queue.append(n.left)
        if n.right is not None:
            queue.append(n.right)
    return res
'''
