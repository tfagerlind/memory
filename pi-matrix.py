import mpmath
import random

mpmath.mp.dps = 1000

def nth_decimal(n):
    return str(mpmath.pi)[1+n]

l = [x for x in range(30)]

random.shuffle(l)

while l:
    x = l.pop()
    group = [nth_decimal(1 + x * 5 + 0),
             nth_decimal(1 + x * 5 + 1),
             nth_decimal(1 + x * 5 + 2),
             nth_decimal(1 + x * 5 + 3),
             nth_decimal(1 + x * 5 + 4)]
    print("".join(group))
