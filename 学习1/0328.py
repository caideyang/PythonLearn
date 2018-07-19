"""
author:caideyang
date:2018-03-29
function"实现减减乘除

"""
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# print(power(3,5))