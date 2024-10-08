#!/usr/bin/env python3
""" Task 1 """
import asyncio
import random
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Task 1"""
    delays_list = []
    delay_task = asyncio.create_task(wait_random(max_delay))
    for i in range(n):
        delays_list.append(await delay_task)
    return sorted(delays_list)
