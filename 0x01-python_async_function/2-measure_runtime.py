#!/usr/bin/env python3
""" Task 2 """
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Task 2"""

    # seconds = await wait_n(n, max_delay) # this is wrong bec

    # the await keywrod can be used to run async function
    # inside another async function , but
    # the function right here is not an async one

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.time() - start_time

    return elapsed_time / n
