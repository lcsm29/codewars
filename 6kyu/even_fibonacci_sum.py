#  Even Fibonacci Sum
#  6 kyu
#  https://www.codewars.com/kata/55688b4e725f41d1e9000065
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def even_fib(m):
    if m <= 2: return 0
    a, b = 1, 2
    sum_even = 2
    while 1:
        a, b = b, a+b
        if b > m:
            return sum_even
        if b % 2 == 0:
            sum_even += b


#    _               _                          _   _
#   | |             | |                        | | (_)
#   | |__   ___  ___| |_   _ __  _ __ __ _  ___| |_ _  ___ ___
#   | '_ \ / _ \/ __| __| | '_ \| '__/ _` |/ __| __| |/ __/ _ \
#   | |_) |  __/\__ \ |_  | |_) | | | (_| | (__| |_| | (_|  __/
#   |_.__/ \___||___/\__| | .__/|_|  \__,_|\___|\__|_|\___\___|
#                         | |  written by
#                         |_|  https://codewars.com/users/BartBee
'''BartBee
def even_fib(m):
    x,y = 0, 1
    counter = 0
    while y < m:
        if y % 2 == 0:
            counter += y
        x,y = y, x+ y
    return counter
'''
