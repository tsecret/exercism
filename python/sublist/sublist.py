"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

from typing import List

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def is_in(l1: List[int], l2: List[int]) -> bool:
  for i in range(len(l1) - len(l2) + 1):
        if not l2 or l2 == l1[i : i + len(l2)]:
            return True
  return False


def sublist(list_one: List[int], list_two: List[int]):

    if list_one == list_two:
      return 3
    elif is_in(list_one, list_two):
      return 2
    elif is_in(list_two, list_one):
      return 1
    else:
      return 4
