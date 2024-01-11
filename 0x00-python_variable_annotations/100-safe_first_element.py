#!/usr/bin/env python3
"""a type-annotated function"""
from typing import Union, Any, Sequence, Iterable


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """a type-annotated function"""
    if lst:
        return lst[0]
    else:
        return None
