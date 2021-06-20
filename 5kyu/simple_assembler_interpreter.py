#  Simple assembler interpreter
#  5 kyu
#  https://www.codewars.com/kata/58e24788e24ddee28e000053
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def simple_assembler(program):
    def leap(d, ops, key):
        num_iter = abs(d[key] // sum([1 if op == f'inc {key}' 
                                  else -1 if op == f'dec {key}'
                                  else  0 for op in ops]))
        count = {k: 0 for k in d.keys()}
        for op in ops:
            count[op.split()[1]] += 1 if op.split()[0] == 'inc' else -1        
        return {k: v + count[k]*num_iter for k, v in d.items()}
    ans = {}
    i = 0
    while i < len(program):
        op, k, v = (program[i] + ' dummy').split()[:3]
        if op == 'mov': ans[k] = ans[v] if v in ans else int(v)
        if op == 'inc': ans[k] += 1
        if op == 'dec': ans[k] -= 1
        if op == 'jnz' and (ans[k] if k in ans else int(k)):
            if all(0 if 'mov' in op or 'jnz' in op else 1 
                            for op in program[i + int(v):i]) and int(v) < 0:
                ans = leap(ans, program[i + int(v):i], k)
            else:
                i += int(v)
            continue
        i += 1
    return ans


if __name__ == '__main__':
    basic_tests = [
        ['simple_assembler', ('mov a 5\ninc a\ndec a\n'
                            + 'dec a\njnz a -2\ninc a').splitlines(), 
                            {'a': 1}],
        ['simple_assembler', ('mov c 12\nmov b 0\nmov a 200\ndec a\ninc b\n'
                            + 'jnz a -2\ndec c\nmov a b\njnz c -5\njnz 0 1\n'
                            + 'mov c a').splitlines(),
                            {'a': 409600, 'c': 409600, 'b': 409600}],
        ['simple_assembler', ('mov a 1\nmov b 1\nmov c 0\nmov d 26\njnz c 2\n'
                            + 'jnz 1 5\nmov c 7\ninc d\ndec c\njnz c -2\n'
                            + 'mov c a\ninc a\ndec b\njnz b -2\nmov b c\n'
                            + 'dec d\njnz d -6\nmov c 18\nmov d 11\ninc a\n'
                            + 'dec d\njnz d -2\ndec c\njnz c -5').splitlines(),
                            {'a': 318009, 'b': 196418, 'c': 0, 'd': 0}],
    ]
    for test in basic_tests:
        fn_name, n, expected = test
        result = globals()[fn_name](n)
        print(f'{fn_name}("{n}") returns {result}'
              f'{f", expected: {expected}" if result != expected else ""}')


#    _               _                          _   _
#   | |             | |                        | | (_)
#   | |__   ___  ___| |_   _ __  _ __ __ _  ___| |_ _  ___ ___
#   | '_ \ / _ \/ __| __| | '_ \| '__/ _` |/ __| __| |/ __/ _ \
#   | |_) |  __/\__ \ |_  | |_) | | | (_| | (__| |_| | (_|  __/
#   |_.__/ \___||___/\__| | .__/|_|  \__,_|\___|\__|_|\___\___|
#                         | |  written by
#                         |_|  https://codewars.com/users/daddepledge
'''daddepledge
def simple_assembler(program):
    d, i = {}, 0
    while i < len(program):
        cmd, r, v = (program[i] + ' 0').split()[:3]
        if cmd == 'inc': d[r] += 1
        if cmd == 'dec': d[r] -= 1        
        if cmd == 'mov': d[r] = d[v] if v in d else int(v)
        if cmd == 'jnz' and (d[r] if r in d else int(r)): i += int(v) - 1
        i += 1
    return d
'''
