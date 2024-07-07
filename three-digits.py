#!/bin/env python
import os
import random
import sys
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def from_string(s):
    return int(s)


def to_string(n):
    return str(n).zfill(3)


if len(sys.argv) != 3:
    print("Try ./three-digits.py 003 020")
    exit(1)

first = from_string(int(sys.argv[1]))
last = from_string(int(sys.argv[2]))

numbers = list(range(first, last + 1))
random.shuffle(numbers)

old_probe = None
count = 0
clear()

while numbers:

    new_probe = numbers.pop()
    print(to_string(new_probe))
    input()
    clear()

    if old_probe is not None:
        response = from_string(input())

        if response != old_probe:
            print(f"Wrong! Correct: {old_probe}")
            print(f"Number of correct answers: {count}")
            exit(0)

        count += 1

        clear()

    old_probe = new_probe


if old_probe is not None:
    response = from_string(input())

    if response != old_probe:
        print(f"Wrong! Correct: {old_probe}")
        print(f"Number of correct answers: {count}")
        exit(0)

clear()

print("Greeat! You did it!")
