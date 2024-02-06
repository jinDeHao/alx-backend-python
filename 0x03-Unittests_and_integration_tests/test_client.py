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
from fixtures import TEST_PAYLOAD


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
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_property:
            mock_property.return_value = {"de hao": "idhmaid",
                                          "repos_url": "omar"}
            inst = GithubOrgClient("idh")
            result = inst._public_repos_url
            self.assertEqual(result, "omar")

    @patch('client.get_json')
    def test_public_repos(self, mock_get: Mock):
        """
        More patching
        """
        mock_get.return_value = [{"name": "dehao",
                                  "dehao asks": "are you stupid bro"}]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_property:
            mock_property.return_value = "no repos_url for you, stupid!"
            inst = GithubOrgClient("idh")
            result = inst.public_repos()
            self.assertEqual(result[0], "dehao")
            mock_property.assert_called_once()
            mock_get.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self,
                         repo: Dict[str, Dict[str, str]],
                         license_key: str,
                         result: bool):
        """
        Parameterize
        """
        self.assertEqual(GithubOrgClient("idh").has_license(repo, license_key),
                         result)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test: fixtures
    """
    @classmethod
    def setUpClass(cls) -> None:
        """sets up and run the class"""
        my_payload = {
            'https://api.github.com/orgs/google': TEST_PAYLOAD[0][0],
            'https://api.github.com/orgs/google/repos': TEST_PAYLOAD[0][1],
        }

        def get_payload(url):
            """get the payload by mocking it"""
            return Mock(**{'json.return_value\
': my_payload[url]}) if url in my_payload else None

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self):
        """Integration tests"""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            TEST_PAYLOAD[0][2],
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the fixtures after done with testing"""
        cls.get_patcher.stop()
