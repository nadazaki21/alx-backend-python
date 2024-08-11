#!/usr/bin/env python3
""" Task 8 """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""

    def inner_fun(x: float) -> float:
        return x * multiplier

    return inner_fun
