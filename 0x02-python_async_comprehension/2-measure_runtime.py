#!/usr/bin/env python3
"""Async measure runtime"""

import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Async measure runtime"""
    initial_moment = time()
    gather_param = [async_comprehension()]*4
    await asyncio.gather(*gather_param)
    return time() - initial_moment
