#!/usr/bin/env python3
""" Task 3 """
import asyncio
import random
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int):
    """Task 3"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
