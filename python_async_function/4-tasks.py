#!/usr/bin/env python3
"""Task 3"""

from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Wait """
    return_list = []
    for i in range(n):
        return_list.append(await wait_random(max_delay))
    return sorted(return_list)
