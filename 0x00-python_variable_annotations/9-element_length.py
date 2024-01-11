#!/usr/bin/env python3
"""a type-annotated function"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """a type-annotated function"""
    return [(i, len(i)) for i in lst]
