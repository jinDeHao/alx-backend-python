#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Dict, Tuple, Any


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self,
                               nested_map: Dict[str, Any],
                               path: Tuple[str],
                               result):
        """test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Dict[str, Any],
                                         path: Tuple[str]):
        """test access_nested_map_exception function"""
        try:
            access_nested_map(nested_map, path)
        except Exception:
            self.assertRaises(KeyError)
