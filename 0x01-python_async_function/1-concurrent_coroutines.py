#!/usr/bin/env python3
"""async coroutine"""

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """wait many times"""
    my_list: list = []
    while True:
        try:
            if my_list[n - 1]:
                return my_list
        except IndexError:
            t = await wait_random(max_delay)
            my_list.append(t)
