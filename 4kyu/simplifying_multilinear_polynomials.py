#  Simplifying multilinear polynomials
#  4 kyu
#  https://www.codewars.com/kata/55f89832ac9a66518f000118
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def simplify(poly):
    def simplified(expression: str) -> dict:
        '''Returns simplified, but unsorted expression in a dictionary

            Args:
                expression (str) -> multilinear polynomial

            Returns:
                exp (dict) -> variables (str): coefficients (int)
        '''
        tmp = []
        nums_and_ops = '0 1 2 3 4 5 6 7 8 9 0 + -'.split()
        for e in expression.replace('+', ' +').replace('-', ' -').split():
            variables = nums = ops = ''
            for i, c in reversed(list(enumerate(e))):
                if c in nums_and_ops and nums == '' and ops == '':
                    variables = ''.join(sorted(e[i + 1:]))
                if c in '0123456789': nums += c
                if c in '+-': ops += c
                if i == 0:
                    if variables == '' and nums == '':
                        variables = ''.join(sorted(e))
                    if nums == '': nums = '1'
            tmp.append([variables, int(ops + nums[::-1])])
        exp = {t[0]: 0 for t in tmp}
        for t in tmp:
            exp[t[0]] += t[1]
        for k, v in exp.copy().items():
            if v == 0:
                exp.pop(k)
        return exp
    lexico_dct = dict(sorted(simplified(poly).items(), key=lambda x: x[0]))
    sorted_lst = sorted([[str(v), k] for k, v in lexico_dct.items()], key=lambda s: len(s[1]))
    with_plus_wo_one = [[l[0] if l[0][0] == '-' else '+' + l[0] if l[0] != '1' else '+', l[1]] for l in sorted_lst]
    remove_minus_one = [l if l[0] != '-1' else ['-', l[1]] for l in with_plus_wo_one]
    final_expression = ''
    for i, exp in enumerate(remove_minus_one):
        if i == 0 and exp[0][0] == '+':
            final_expression += exp[0].replace('+','') + exp[1]
        else:
            final_expression += exp[0] + exp[1]
    return final_expression


if __name__ == '__main__':
    basic_tests = [
        ['simplify', "dc+dcba", "cd+abcd"],  # Test reduction by equivalence
        ['simplify', "2xy-yx", "xy"],
        ['simplify', "-a+5ab+3a-c-2a", "-c+5ab"],
        ['simplify', "-abc+3a+2ac", "3a+2ac-abc"],  # Test monomial length ordering
        ['simplify', "xyz-xz", "-xz+xyz"],
        ['simplify', "a+ca-ab", "a-ab+ac"],  # Test lexicographic ordering
        ['simplify', "xzy+zby", "byz+xyz"],
        ['simplify', "-y+x", "x-y"],  # Test no leading +
        ['simplify', "y-x", "-x+y"]
    ]
    for test in basic_tests:
        fn_name, poly, expected = test
        result = globals()[fn_name](poly)
        print(f'{fn_name}("{poly}") returns "{result}"'
              f'{f", expected: {expected}" if result != expected else ""}')


#    _               _                          _   _
#   | |             | |                        | | (_)
#   | |__   ___  ___| |_   _ __  _ __ __ _  ___| |_ _  ___ ___
#   | '_ \ / _ \/ __| __| | '_ \| '__/ _` |/ __| __| |/ __/ _ \
#   | |_) |  __/\__ \ |_  | |_) | | | (_| | (__| |_| | (_|  __/
#   |_.__/ \___||___/\__| | .__/|_|  \__,_|\___|\__|_|\___\___|
#                         | |  written by
#                         |_|  https://codewars.com/users/brianpck
'''brianpck
def simplify(poly):
    # I'm feeling verbose today
    
    # get 3 parts (even if non-existent) of each term: (+/-, coefficient, variables)
    import re
    matches = re.findall(r'([+\-]?)(\d*)([a-z]+)', poly)
    
    # get the int equivalent of coefficient (including sign) and the sorted variables (for later comparison)
    expanded = [[int(i[0] + (i[1] if i[1] != "" else "1")), ''.join(sorted(i[2]))] for i in matches]
    
    # get the unique variables from above list. Sort them first by length, then alphabetically
    variables = sorted(list(set(i[1] for i in expanded)), key=lambda x: (len(x), x))
    
    # get the sum of coefficients (located in expanded) for each variable
    coefficients = {v:sum(i[0] for i in expanded if i[1] == v) for v in variables}
    
    # clean-up: join them with + signs, remove '1' coefficients, and change '+-' to '-'
    return '+'.join(str(coefficients[v]) + v for v in variables if coefficients[v] != 0).replace('1','').replace('+-','-')
'''
