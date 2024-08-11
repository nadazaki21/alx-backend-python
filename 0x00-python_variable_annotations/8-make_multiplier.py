#!/usr/bin/env python3
""" Task 8 """


def make_multiplier(multiplier: float) -> float:
    """returns a function that multiplies a float by multiplier"""

    def inner_fun(x: float) -> float:
        return x * multiplier

    return inner_fun
