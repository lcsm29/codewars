#  Sum of odd numbers
#  7 kyu
#  https://www.codewars.com/kata/55fd2d567d94ac3bc9000064
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def row_sum_odd_numbers(n: int) -> int:
    ''' Returns the sum of odd numbers in n_th row 
        of the triangle of consecutive odd numbers

        Args: 
            n (int) -> index of the row, starting index 1
        
        Returns:
            n ** 3 (int) -> the sum of odd numbers in the n_th row
    '''
    assert type(n) == int and n > 0, 'n should be a positve integer'
    return n ** 3


if __name__ == '__main__':
    basic_tests = [
        ['row_sum_odd_numbers', 1, 1],
        ['row_sum_odd_numbers', 42, 74_088]
    ]
    for test in basic_tests:
        fn_name, n, expected = test
        result = globals()[fn_name](n)
        print(f'{fn_name}({n}) returns {result}'
              f'{f", expected: {expected}" if result != expected else ""}')


#    _               _                          _   _
#   | |             | |                        | | (_)
#   | |__   ___  ___| |_   _ __  _ __ __ _  ___| |_ _  ___ ___
#   | '_ \ / _ \/ __| __| | '_ \| '__/ _` |/ __| __| |/ __/ _ \
#   | |_) |  __/\__ \ |_  | |_) | | | (_| | (__| |_| | (_|  __/
#   |_.__/ \___||___/\__| | .__/|_|  \__,_|\___|\__|_|\___\___|
#                         | |  written by
#                         |_|  https://www.codewars.com/users/CIS%20122
'''CIS 122
def row_sum_odd_numbers(n):
    #your code here
    return n ** 3
'''
