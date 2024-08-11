#!/usr/bin/env python3
""" Taks 6 """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes a list mxd_lst of integers
    and floats and returns their sum as a float."""
    sum = 0
    for i in mxd_lst:
        sum += i

    return float(sum)
