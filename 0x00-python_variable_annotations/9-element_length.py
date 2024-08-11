#!/usr/bin/env python3
""" Task 9 """
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Iterable[Sequence], int]]:
    """returns a list of tuples"""
    return [(i, len(i)) for i in lst]
