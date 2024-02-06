#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock, patch
from parameterized import parameterized
from typing import Dict, Tuple, Any


class TestAccessNestedMap(unittest.TestCase):
    """
    Test Access Nested Map
    """

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


class TestGetJson(unittest.TestCase):
    """Test Get Json Method"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self,
                      url: str,
                      payload: Dict[str, bool],
                      mock_get: Mock):
        """Mock HTTP calls"""
        mock_get.return_value.json.return_value = payload
        result = get_json(url)
        self.assertEqual(result, payload)
        mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """Test Memoize"""

    def test_memoize(self):
        """test memoize decorator"""
        class TestClass:
            """
            Test class
            """
            def __init__(self) -> None:
                """
                initlaize instance attributes
                """
                self.a_method_call = 0

            def a_method(self):
                """targeted method"""
                self.a_method_call += 1
                return 42

            @memoize
            def a_property(self):
                """memoize method"""
                return self.a_method()

        test_obj = TestClass()
        call_method_1 = test_obj.a_property
        call_method_2 = test_obj.a_property

        self.assertEqual(call_method_1, call_method_2)
        self.assertEqual(call_method_1, 42)
        self.assertEqual(test_obj.a_method_call, 1)
