#!/usr/bin/env python3
""" Task 8 """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Make multiplier"""
    def multiplier_function(number: float) -> float:
        """Mult func"""
        return number * multiplier
    return multiplier_function
