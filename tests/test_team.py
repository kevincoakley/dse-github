#!/usr/bin/env python

from github import Github
from mock import MagicMock
from mock import patch
import dsegithub.team
import unittest


class OrganizationTestCase(unittest.TestCase):
    def setUp(self):
        pass

    @patch.object(Github, "get_organization")
    def test_get_team(self, mock_github):
        fake_team = MagicMock()
        fake_team.name = "Test Team"
        mock_github().get_teams.return_value = [fake_team]

        g = Github("abc123")
        organization = g.get_organization("test")

        team = dsegithub.team.create_get_team(organization, "Test Team")
        self.assertEqual(team.name, "Test Team")

    @patch.object(Github, "get_organization")
    def test_create_team(self, mock_github):
        bad_team = MagicMock()
        bad_team.name = "Bad Team"
        mock_github().get_teams.return_value = [bad_team]

        create_team = MagicMock()
        create_team.name = "Test Team"
        mock_github().create_team.return_value = create_team

        g = Github("abc123")
        organization = g.get_organization("test")

        team = dsegithub.team.create_get_team(organization, "Test Team")
        self.assertEqual(team.name, "Test Team")
