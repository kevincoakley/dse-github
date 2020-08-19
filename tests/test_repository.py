#!/usr/bin/env python

from github import Github
from github.GithubException import GithubException
from github.GithubException import UnknownObjectException
from mock import MagicMock
from mock import patch
import dsegithub.organization
import dsegithub.repository
import unittest


class RepositoryTestCase(unittest.TestCase):
    def setUp(self):
        pass

    @patch.object(Github, "get_organization")
    def test_get_repository_does_not_exist(self, mock_github):
        mock_github().get_repo.side_effect = UnknownObjectException(status=404, data="")

        g = Github("abc123")
        org = dsegithub.organization.get_organization(g, "test")

        repository = dsegithub.repository.get_repository(org, "test-repo")
        self.assertIsNone(repository)

    @patch.object(Github, "get_organization")
    def test_get_repository_exist(self, mock_github):
        fake_repository = MagicMock()
        fake_repository.name = "test-repo"
        mock_github().get_repo.return_value = fake_repository

        g = Github("abc123")
        org = dsegithub.organization.get_organization(g, "test")

        repository = dsegithub.repository.get_repository(org, "test-repo")
        self.assertEqual(repository.name, "test-repo")

    @patch.object(Github, "get_organization")
    def test_create_repository_exists(self, mock_github):
        mock_github().create_repo.side_effect = GithubException(status=422, data="")

        g = Github("abc123")
        org = dsegithub.organization.get_organization(g, "test")

        repository = dsegithub.repository.create_repository(org, "test-repo")
        self.assertIsNone(repository)

    @patch.object(Github, "get_organization")
    def test_create_repository(self, mock_github):
        fake_repository = MagicMock()
        fake_repository.name = "test-repo"
        mock_github().create_repo.return_value = fake_repository

        g = Github("abc123")
        org = dsegithub.organization.get_organization(g, "test")

        repository = dsegithub.repository.create_repository(org, "test-repo")
        self.assertEqual(repository.name, "test-repo")