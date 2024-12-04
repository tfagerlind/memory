import random
import sys
import time
import mpmath

GROUP_SIZE = 5

room_start = int(sys.argv[1]) - 1
room_count = int(sys.argv[2])

group_start = 5 * room_start
group_count = 5 * room_count

# ensure that we have enough precision by multiplying with two
mpmath.mp.dps = 2 * GROUP_SIZE * (group_start + group_count)

print(f"This challenge will test {5 * group_count} decimals of pi,")
print(f"ranging from decimal {5 * group_start} to")
print(f"decimal {5 * group_start + 5 * group_count}.")

def nth_decimal(n):
    return str(mpmath.pi)[1+n]


group_indices = [index for index in range(group_start,
                                          group_start + group_count)]

random.shuffle(group_indices)


def get_group(index):
    return [nth_decimal(1 + index * 5 + decimal_index)
            for decimal_index
            in range(5)]


def group_as_string(group):
    return "".join(group)


def check_and_respond_to_answer(actual, expected):
    if actual == expected:
        print("Correct!")
        return True
    else:
        print(f"Incorrect. Correct answer was {expected}.")
        return False


total_question_count = len(group_indices)
incorrect_answers = 0

while group_indices:
    print("Progress: {}/{}\n".format(total_question_count - len(group_indices),
                                      total_question_count))

    index = group_indices.pop()
    group = get_group(index=index)
    print(group_as_string(group))

    if index == group_start:
        before = "None"
    else:
        before = get_group(index=index-1)

    if index == group_start + group_count - 1:
        after = "None"
    else:
        after = get_group(index=index+1)


    before_as_string = group_as_string(before)
    after_as_string = group_as_string(after)

    guess = input("Before: ")

    correct = check_and_respond_to_answer(guess.strip(),
                                          before_as_string)

    if not correct:
        incorrect_answers += 1

    guess = input("After: ")

    correct = check_and_respond_to_answer(guess.strip(),
                                          after_as_string)

    if not correct:
        incorrect_answers += 1

    time.sleep(1)
    print("")

print(f"Complete! Number of incorrect answers: {incorrect_answers}")
