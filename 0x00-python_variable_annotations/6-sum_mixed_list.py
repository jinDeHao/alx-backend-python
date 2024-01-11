#!/usr/bin/env python3
"""a type-annotated function"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """a type-annotated function"""
    sum: float = 0.0
    for n in mxd_lst:
        sum += float(n)
    return sum


print(sum_mixed_list.__annotations__)
mixed = [5, 4, 3.14, 666, 0.99]
ans = sum_mixed_list(mixed)
print(ans == sum(mixed))
print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))
