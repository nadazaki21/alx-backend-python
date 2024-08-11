#!/usr/bin/env python3
""" Task 5 """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """which takes a list input_list of floats as
    argument and returns their sum as a float."""

    sum = 0
    for i in input_list:
        sum += i

    return sum
