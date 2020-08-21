#!/usr/bin/env python

from github import Github
from github.GithubException import UnknownObjectException
from mock import patch
import dsegithub.shell as shell
import sys
import unittest


class ShellTestCase(unittest.TestCase):
    def setUp(self):
        self.csv = [
            {"Repository": "test-repo1", "Cohort": "test", "Username": "test1"},
            {"Repository": "test-repo2", "Cohort": "test", "Username": "test2"},
        ]

    @patch("dsegithub.csv.open", create=True)
    @patch("csv.DictReader")
    @patch.object(Github, "get_user", autospec=True)
    @patch.object(Github, "get_organization", autospec=True)
    def test_main_command_line_arguments(
        self, mock_organization, mock_user, mock_csv_reader, mock_open
    ):
        mock_csv_reader.return_value = self.csv

        #
        # Test debug
        #
        with patch.object(
            sys,
            "argv",
            [
                "dse-github",
                "--access-token",
                "abc123",
                "--file",
                "test.csv",
                "--debug",
            ],
        ):
            # self.assertRegex(shell.main(), "^\nswift-archive requires")
            shell.main()

        #
        # Test access-token
        #
        with patch.object(
            sys,
            "argv",
            ["dse-github", "--access-token", "abc123", "--file", "test.csv",],
        ):
            shell.main()

        #
        # Test username and password
        #
        with patch.object(
            sys,
            "argv",
            [
                "dse-github",
                "--username",
                "user",
                "--password",
                "pass",
                "--file",
                "test.csv",
            ],
        ):
            shell.main()

    @patch("dsegithub.csv.open", create=True)
    @patch("csv.DictReader")
    @patch.object(Github, "get_user", autospec=True)
    @patch.object(Github, "get_organization")
    def test_main_repo_does_not_exist(
        self, mock_organization, mock_user, mock_csv_reader, mock_open
    ):
        mock_csv_reader.return_value = self.csv
        mock_organization().get_repo.side_effect = UnknownObjectException(
            status=404, data=""
        )

        with patch.object(
            sys,
            "argv",
            ["dse-github", "--access-token", "abc123", "--file", "test.csv",],
        ):
            shell.main()

    @patch("dsegithub.csv.open", create=True)
    @patch("csv.DictReader")
    @patch.object(Github, "get_user", autospec=True)
    @patch.object(Github, "get_organization")
    def test_main_user_does_not_exist(
        self, mock_organization, mock_user, mock_csv_reader, mock_open
    ):
        mock_csv_reader.return_value = self.csv
        mock_user.side_effect = UnknownObjectException(404, "")

        with patch.object(
            sys,
            "argv",
            ["dse-github", "--access-token", "abc123", "--file", "test.csv",],
        ):
            shell.main()
