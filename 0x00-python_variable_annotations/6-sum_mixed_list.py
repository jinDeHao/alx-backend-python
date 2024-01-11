#!/usr/bin/env python3
"""a type-annotated function"""
from typing import Union


def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    """a type-annotated function"""
    sum: float = 0.0
    for n in mxd_lst:
        sum += float(n)
    return sum
