#!/usr/bin/env python3
"""a type-annotated function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """a type-annotated function"""
    sum: float = 0.0
    for n in input_list:
        sum += n
    return sum
