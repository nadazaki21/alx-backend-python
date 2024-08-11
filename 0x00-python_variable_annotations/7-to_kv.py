#!/usr/bin/env python3
""" Task 7 """


def to_kv(k: str, v: int | float) -> tuple:
    return (k, float(v**2))