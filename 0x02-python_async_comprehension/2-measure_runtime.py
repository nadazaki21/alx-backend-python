#!/usr/bin/env python3
""" Task 2 - Measure Runtime """

import asyncio
import time


async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime():
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    finish_time = time.time()
    return finish_time - start_time
