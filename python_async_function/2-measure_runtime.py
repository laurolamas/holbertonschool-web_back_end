#!/usr/bin/env python3
"""Task 2"""

import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Wait """
    return_list = asyncio.run(wait_n(n, max_delay))
    return sum(return_list) / n
