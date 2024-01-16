#!/usr/bin/env python3
"""wait then yield"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """wait then yield"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
