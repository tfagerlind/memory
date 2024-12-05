#!/bin/env python3
import random
import time
import mpmath
import click


GROUP_SIZE = 5


def nth_decimal(n):
    # Probably enough precision, as long as we only care about the first 10000
    # decimals. Rounding issues that can happen when there are multiple nines
    # in a row, for example, and that is something we need to keep in mind.
    if n > 10000:
        raise NotImplementedError("We don't use enough precison"
                                  " to be able to guarantee the"
                                  " reliability of that big numbers.")
    with mpmath.mp.workdps(20000):
        return str(mpmath.pi)[1+n]


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


def main(room_start, room_count):
    room_start = room_start - 1  # make zero-indexed

    group_start = 5 * room_start
    group_count = 5 * room_count

    print(f"This challenge will test {5 * group_count} decimals of pi,")
    print(f"ranging from decimal {5 * group_start} to")
    print(f"decimal {5 * group_start + 5 * group_count}.")

    group_indices = [index for index in range(group_start,
                                              group_start + group_count)]

    random.shuffle(group_indices)

    total_question_count = len(group_indices)
    incorrect_answers = 0

    while group_indices:
        remaining_question_count = total_question_count - len(group_indices)
        print(f"Progress: {remaining_question_count}/{total_question_count}")

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


@click.command()
@click.argument('room_start', type=int)
@click.argument('room_count', type=int)
def pi_matrix(room_start, room_count):
    """Challenge your pi decimal skills."""
    main(room_start, room_count)


if __name__ == '__main__':
    pi_matrix()
