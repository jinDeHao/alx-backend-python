#!/usr/bin/env python3
"""a type-annotated function"""
import typing


class Mytyping:
    """help class"""
    T = typing.TypeVar('T')


def safely_get_value(
    dct: typing.Mapping,
    key: typing.Any,
    default: typing.Union[Mytyping.T, None] = None
) -> typing.Union[typing.Any, Mytyping.T]:
    """a type-annotated function"""
    if key in dct:
        return dct[key]
    else:
        return default
