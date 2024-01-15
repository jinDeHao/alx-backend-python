#!/usr/bin/env python3
"""async tach"""
from time import time
import asyncio

from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """function async"""
    my_list: List[float] = []
    while True:
        try:
            my_list[n - 1]
            return sorted(my_list)
        except IndexError:
            my_list.append(await task_wait_random(max_delay))
