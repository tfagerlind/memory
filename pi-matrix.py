#!/bin/env python3
from dataclasses import dataclass
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


@dataclass
class Group:
    index: int

    def __repr__(self):
        return ("None"
                if self.index == -1
                else group_as_string(get_group(self.index)))

    def before(self):
        return self if self.index == -1 else Group(self.index-1)

    def after(self):
        return Group(self.index+1)


def check_and_respond_to_answer(actual, expected):
    if actual == expected:
        print("Correct!")
        return True
    else:
        print(f"Incorrect. Correct answer was {expected}.")
        return False


def get_random_groups(group_start, group_count):
    group_indices = [index for index in range(group_start,
                                              group_start + group_count)]

    random.shuffle(group_indices)

    groups = [Group(index) for index in group_indices]

    return groups


def main(room_start, room_count):
    room_start = room_start - 1  # make zero-indexed

    group_start = 5 * room_start
    group_count = 5 * room_count

    print(f"This challenge will test {5 * group_count} decimals of pi,")
    print(f"ranging from decimal {5 * group_start} to")
    print(f"decimal {5 * group_start + 5 * group_count}.")

    groups = get_random_groups(group_start, group_count)

    total_question_count = group_count
    incorrect_answers = 0

    for index, group in enumerate(groups):
        completed_question_count = index
        print(f"Progress: {completed_question_count}/{total_question_count}")

        print(str(group))

        guess = input("Before: ")

        correct = check_and_respond_to_answer(guess.strip(),
                                              str(group.before()))

        if not correct:
            incorrect_answers += 1

        guess = input("After: ")

        correct = check_and_respond_to_answer(guess.strip(),
                                              str(group.after()))

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
