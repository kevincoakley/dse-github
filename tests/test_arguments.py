#!/usr/bin/env python

import unittest
import dsegithub.arguments


class ArgumentsTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_no_authentication(self):
        # Test that not including username, password or access_token will cause a sys.exit(2)
        with self.assertRaises(SystemExit) as se:
            dsegithub.arguments.parse_arguments(
                ["--team", "test", "--file", "test.csv"]
            )
        self.assertEqual(se.exception.code, 2)

    def test_username_only(self):
        # Test that including only username will cause a sys.exit(2)
        with self.assertRaises(SystemExit) as se:
            dsegithub.arguments.parse_arguments(
                ["--username", "user", "--team", "test", "--file", "test.csv",]
            )
        self.assertEqual(se.exception.code, 2)

    def test_password_only(self):
        # Test that including only password will cause a sys.exit(2)
        with self.assertRaises(SystemExit) as se:
            dsegithub.arguments.parse_arguments(
                ["--password", "pass", "--team", "test", "--file", "test.csv",]
            )
        self.assertEqual(se.exception.code, 2)

    def test_username_password(self):
        # Test that including only password will cause a sys.exit(2)
        args = dsegithub.arguments.parse_arguments(
            [
                "--username",
                "user",
                "--password",
                "pass",
                "--team",
                "test",
                "--file",
                "test.csv",
            ]
        )
        self.assertEqual(args.username, "user")
        self.assertEqual(args.password, "pass")
        self.assertIsNone(args.access_token)

    def test_access_token(self):
        args = dsegithub.arguments.parse_arguments(
            ["--access-token", "abc123", "--team", "test", "--file", "test.csv",]
        )
        self.assertIsNone(args.username)
        self.assertIsNone(args.password)
        self.assertEqual(args.access_token, "abc123")
