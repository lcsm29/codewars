#  Multiples of 3 or 5
#  6 kyu
#  https://www.codewars.com/kata/514b92a657cdc65150000006
#
#               w r i t t e n    b y
#   oooo        https://github.com/lcsm29        .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def solution(number):
    def gauss_sum(num):
        num_mults = number // num
        if number % num == 0:
            num_mults = number // num - 1
        gsum = 0.5 * num_mults * (num_mults + 1)
        return int(gsum * num)
    return gauss_sum(3) + gauss_sum(5) - gauss_sum(15)


#    _               _                          _   _
#   | |             | |                        | | (_)
#   | |__   ___  ___| |_   _ __  _ __ __ _  ___| |_ _  ___ ___
#   | '_ \ / _ \/ __| __| | '_ \| '__/ _` |/ __| __| |/ __/ _ \
#   | |_) |  __/\__ \ |_  | |_) | | | (_| | (__| |_| | (_|  __/
#   |_.__/ \___||___/\__| | .__/|_|  \__,_|\___|\__|_|\___\___|
#                         | |  written by
#                         |_|  https://codewars.com/users/zyxwhut
'''zyxwhut
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
'''
