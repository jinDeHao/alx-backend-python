#!/usr/bin/env python3
"""a type-annotated function"""
from typing import Callable


class mult:
    """a type-annotated class"""
    multiplier: float


m = mult()


def fun(multiplier: float) -> float:
    """a type-annotated function"""
    return m.multiplier * multiplier


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """a type-annotated function"""
    m.multiplier = multiplier
    return fun
