import sys
import mpmath
import random

group_count = int(sys.argv[1])

GROUP_SIZE = 5

# ensure that we have enough precision by multiplying with two
mpmath.mp.dps = 2 * GROUP_SIZE * group_count


def nth_decimal(n):
    return str(mpmath.pi)[1+n]


group_indices = [index for index in range(group_count)]

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

    if index == group_count - 1:
        after = "None"
    else:
        after = get_group(index=index+1)


    before_as_string = group_as_string(before)
    after_as_string = group_as_string(after)

    guess = input()

    if guess.strip() == before_as_string:
        print("Correct!")
    else:
        print(f"Incorrect. Correct answer was {before_as_string}.")

    guess = input()

    if guess.strip() == after_as_string:
        print("Correct!")
    else:
        print(f"Incorrect. Correct answer was {after_as_string}.")
