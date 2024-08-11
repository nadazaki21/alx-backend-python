#!/usr/bin/env python3
""" Task 9 """
from typing import List, Tuple, Set


def element_length(lst: str) -> List[Tuple[str, int]]:
    return [(i, len(i)) for i in lst]
