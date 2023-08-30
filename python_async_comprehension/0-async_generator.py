#!/usr/bin/env python3
"""Task 0"""

import random
import time


async def async_generator():
    """Async generator"""
    async for i in range(10):
        random_number = random.uniform(0, 10)
        await time.sleep(1)
        yield(random_number)
