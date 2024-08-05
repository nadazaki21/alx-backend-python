#!/usr/bin/env python3
""" Task 4 """
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Task 4"""
    delays_list = []

    for i in range(n):
        delay_task = task_wait_random(
            max_delay
        )  # task_wait_random should not be called inside a
        # create_task , since it is not async function
        # asyncio.run should not be used inside an async function
        await delay_task
        delays_list.append(delay_task.result())

    return sorted(delays_list)
