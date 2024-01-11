#!/usr/bin/env python3
"""a type-annotated function"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """a type-annotated function"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
