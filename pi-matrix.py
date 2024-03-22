import mpmath
import random

mpmath.mp.dps = 1000

def nth_decimal(n):
    return str(mpmath.pi)[1+n]

group_indices = [index for index in range(30)]

random.shuffle(group_indices)

while group_indices:
    group_index = group_indices.pop()
    group = [nth_decimal(1 + group_index * 5 + decimal_index)
            for decimal_index
            in range(5)]
    group_as_string = "".join(group)
    print(group_as_string)
