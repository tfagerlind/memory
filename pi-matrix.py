#!/bin/env python3
from dataclasses import dataclass
from datetime import datetime
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


def request_group(group):
    """Request group from user.

    Returns the number of errors, i.e a number in the range 0-2

    """

    # ask question to user
    print(str(group))

    # take input
    guess = input("Before: ")

    # check result and respond
    correct_before = check_and_respond_to_answer(guess.strip(),
                                                 str(group.before()))

    # take input
    guess = input("After: ")

    # check result and respond
    correct_after = check_and_respond_to_answer(guess.strip(),
                                                str(group.after()))

    return int(not correct_before) + int(not correct_after)


def main(room_start, room_count):
    # interpret user choices
    room_start = room_start - 1  # make zero-indexed

    group_start = 5 * room_start
    group_count = 5 * room_count

    # Welcome user
    print(f"This challenge will test {5 * group_count} decimals of pi,")
    print(f"ranging from decimal {5 * group_start} to")
    print(f"decimal {5 * group_start + 5 * group_count}.")

    # prepare game
    groups = get_random_groups(group_start, group_count)

    # book keeping
    total_question_count = group_count
    incorrect_answers = 0

    # start game

    # book keeping
    start_time = datetime.now()

    for index, group in enumerate(groups):
        # bookkeeping
        completed_question_count = index

        # show statistics
        print(f"Progress: {completed_question_count}/{total_question_count}")

        error_count = request_group(group)

        incorrect_answers += error_count

        # end question
        time.sleep(1)
        print("")

    # book keeping
    end_time = datetime.now()
    run_time = end_time - start_time
    (minutes, seconds) = divmod(run_time.seconds, 60)
    microseconds = run_time.microseconds

    # summarize results
    print(f"Complete! Number of incorrect answers: {incorrect_answers}")
    print(f"It took {minutes} minutes, {seconds} seconds,"
          f" and {microseconds} microseconds.")


@click.command()
@click.argument('room_start', type=int)
@click.argument('room_count', type=int)
def pi_matrix(room_start, room_count):
    """Challenge your pi decimal skills."""
    main(room_start, room_count)


if __name__ == '__main__':
    pi_matrix()
