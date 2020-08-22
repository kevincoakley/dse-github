#!/usr/bin/env python

from github import Github
from github import NamedUser
from github.GithubException import UnknownObjectException
from mock import MagicMock
from mock import patch
import dsegithub.user
import unittest


class UserTestCase(unittest.TestCase):
    def setUp(self):
        pass

    @patch.object(Github, "get_user", autospec=True)
    def test_get_user(self, mock_github):
        fake_user = MagicMock(spec=NamedUser)
        fake_user.login = "test"

        mock_github.return_value = fake_user

        g = Github("abc123")

        user = dsegithub.user.get_user(g, "test")
        self.assertEqual(user.login, "test")

    @patch.object(Github, "get_user", autospec=True)
    def test_get_unknown_user(self, mock_github):
        mock_github.side_effect = UnknownObjectException(404, "")

        g = Github("abc123")

        self.assertIsNone(dsegithub.user.get_user(g, "test"))
