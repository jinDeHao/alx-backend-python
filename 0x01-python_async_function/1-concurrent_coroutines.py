#!/usr/bin/env python3
"""async coroutine"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait many times"""
    my_list: List[float] = []
    while True:
        try:
            my_list[n - 1]
            return sorted(my_list)
        except IndexError:
            t = await wait_random(max_delay)
            my_list.append(t)


print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
