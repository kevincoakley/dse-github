#!/usr/bin/env python

from github import Github
from github import Organization
from github.GithubException import BadCredentialsException
from github.GithubException import UnknownObjectException
from mock import MagicMock
from mock import patch
import dsegithub.organization as organization
import unittest


class OrganizationTestCase(unittest.TestCase):
    def setUp(self):
        pass

    @patch.object(Github, "get_organization", autospec=True)
    def test_get_organization(self, mock_github):
        fake_organization = MagicMock(spec=Organization)
        fake_organization.name = "test"

        mock_github.return_value = fake_organization

        g = Github("abc123")

        org = organization.get_organization(g, "test")
        self.assertEqual(org.name, "test")

    @patch.object(Github, "get_organization", autospec=True)
    def test_get_bad_credentials(self, mock_github):
        mock_github.side_effect = BadCredentialsException(404, "")

        g = Github("abc123")

        with self.assertRaises(SystemExit) as se:
            organization.get_organization(g, "test")
        self.assertEqual(se.exception.code, "Invalid GitHub Credentials!")

    @patch.object(Github, "get_organization", autospec=True)
    def test_get_unknown_organization(self, mock_github):
        mock_github.side_effect = UnknownObjectException(404, "")

        g = Github("abc123")

        with self.assertRaises(SystemExit) as se:
            organization.get_organization(g, "test")
        self.assertEqual(se.exception.code, "Organization test not found!")
