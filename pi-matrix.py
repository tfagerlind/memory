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


def group_as_string(group):
    return "".join(group)


while group_indices:
    index = group_indices.pop()
    group = get_group(index=index)
    print(group_as_string(group))

    if index == 0:
        before = "None"
    else:
        before = get_group(index=index-1)

    if index == 29:
        after = "None"
    else:
        after = get_group(index=index+1)

    input()

    before_as_string = group_as_string(before)
    after_as_string = group_as_string(after)
    print(f"before: {before_as_string} after: {after_as_string}")
