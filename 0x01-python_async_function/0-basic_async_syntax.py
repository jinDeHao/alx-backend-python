#!/usr/bin/env python3
"""async coroutine"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """async function"""
    t = uniform(0, max_delay)
    await asyncio.sleep(t)
    return t
