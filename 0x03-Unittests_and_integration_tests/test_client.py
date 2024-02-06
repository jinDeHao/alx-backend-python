#!/usr/bin/env python3
"""
Parameterize and patch as decorators
"""
import unittest
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock, patch, PropertyMock
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

    def test_public_repos_url(self):
        """
        Mocking a property
        """
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_property:
            mock_property.return_value = {"de hao": "idhmaid", "repos_url": "omar"}
            inst = GithubOrgClient("idh")
            result = inst._public_repos_url
            self.assertEqual(result, "omar")
