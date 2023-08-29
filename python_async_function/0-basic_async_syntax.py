#!/usr/bin/env python3
"""Task 0"""
import asyncio
import random


async def wait_random(n: int = 10):
    """Wait random"""
    random_float = random.uniform(0.0, n)
    await asyncio.sleep(random_float)
    return random_float
