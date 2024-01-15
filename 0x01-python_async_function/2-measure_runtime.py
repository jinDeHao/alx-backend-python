#!/usr/bin/env python3
"""async coroutine"""
from time import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """function async"""
    initial_time = time()
    asyncio.run(wait_n(n, max_delay))
    return (time() - initial_time) / n
