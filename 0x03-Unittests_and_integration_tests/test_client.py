#!/usr/bin/env python3
"""
Parameterize and patch as decorators
"""
import unittest
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock, patch
from parameterized import parameterized
from typing import Dict, Tuple, Any
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Parameterize and patch as decorators
    """
    @parameterized.expand([
        ("google"),
        ("org"),
    ])
    @patch('client.get_json')
    def test_org(
                 self,
                 org: str,
                 mock_get: Mock):
        """
        test that GithubOrgClient.org
        returns the correct value
        """
        url = f"https://api.github.com/orgs/{org}"
        GithubOrgClient(org).org
        mock_get.assert_called_once_with(url)
