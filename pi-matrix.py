import mpmath
import random

mpmath.mp.dps = 1000

def nth_decimal(n):
    return str(mpmath.pi)[1+n]

group_indices = [index for index in range(30)]

random.shuffle(group_indices)

def get_group(index):
    return [nth_decimal(1 + index * 5 + decimal_index)
            for decimal_index
            in range(5)]

while group_indices:
    index = group_indices.pop()
    group = get_group(index=index)
    group_as_string = "".join(group)
    print(group_as_string)
