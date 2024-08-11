#!/usr/bin/env python3
""" Task 2 advanced (101)"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar("T", contravariant=True)


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
