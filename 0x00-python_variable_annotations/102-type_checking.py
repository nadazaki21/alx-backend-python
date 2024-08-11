#!/usr/bin/env python3
""" Task 3 advaced (102)"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in
    # for in in range(factor):
    #     for item in lst:
    #         zoomed_in.append(item)


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
