#!/usr/bin/env python3
""" Task 7 """
from typing import Tuple


def to_kv(k: str, v: int | float) -> Tuple[str, float]:
    """returns a tuple. The first element of the
    tuple is the string k. The second element is
    the square of the int/float v and should be
    annotated as a float.
    """
    return (k, float(v**2))
