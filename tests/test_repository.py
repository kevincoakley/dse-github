#!/usr/bin/env python

from github import Github
from github.GithubException import GithubException
from github.GithubException import UnknownObjectException
from mock import MagicMock
from mock import patch
import dsegithub.organization
import dsegithub.repository
import dsegithub.user
import unittest


class RepositoryTestCase(unittest.TestCase):
    def setUp(self):
        pass

    @patch.object(Github, "get_organization")
    def test_get_repository_does_not_exist(self, mock_github):
        mock_github().get_repo.side_effect = UnknownObjectException(status=404, data="")

        g = Github("abc123")
        org = dsegithub.organization.get_organization(g, "test")

        self.assertIsNone(dsegithub.repository.get_repository(org, "test-repo"))

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

        self.assertIsNone(dsegithub.repository.create_repository(org, "test-repo"))

    @patch.object(Github, "get_organization")
    def test_create_repository(self, mock_github):
        fake_repository = MagicMock()
        fake_repository.name = "test-repo"
        mock_github().create_repo.return_value = fake_repository

        g = Github("abc123")
        org = dsegithub.organization.get_organization(g, "test")

        repository = dsegithub.repository.create_repository(org, "test-repo")
        self.assertEqual(repository.name, "test-repo")

    @patch.object(Github, "get_organization")
    def test_create_readme(self, mock_github):
        mock_github().create_repo().get_readme.side_effect = UnknownObjectException(
            status=404, data=""
        )

        g = Github("abc123")
        org = dsegithub.organization.get_organization(g, "test")

        repository = dsegithub.repository.create_repository(org, "test-repo")
        self.assertTrue(dsegithub.repository.create_readme(repository))

    @patch.object(Github, "get_organization")
    def test_create_readme_failed(self, mock_github):
        mock_github().create_repo().get_readme.side_effect = UnknownObjectException(
            status=404, data=""
        )
        mock_github().create_repo().create_file.side_effect = GithubException(
            status=422, data=""
        )

        g = Github("abc123")
        org = dsegithub.organization.get_organization(g, "test")

        repository = dsegithub.repository.create_repository(org, "test-repo")
        self.assertFalse(dsegithub.repository.create_readme(repository))

    @patch.object(Github, "get_organization")
    def test_create_readme_exists(self, mock_github):
        g = Github("abc123")
        org = dsegithub.organization.get_organization(g, "test")

        repository = dsegithub.repository.create_repository(org, "test-repo")
        self.assertFalse(dsegithub.repository.create_readme(repository))

    @patch.object(Github, "get_organization")
    def test_create_folder(self, mock_github):
        mock_github().create_repo().get_contents.side_effect = UnknownObjectException(
            status=404, data=""
        )

        g = Github("abc123")
        org = dsegithub.organization.get_organization(g, "test")

        repository = dsegithub.repository.create_repository(org, "test-repo")
        self.assertTrue(dsegithub.repository.create_folder(repository, "test-folder"))

    @patch.object(Github, "get_organization")
    def test_create_folder_failed(self, mock_github):
        mock_github().create_repo().get_contents.side_effect = UnknownObjectException(
            status=404, data=""
        )
        mock_github().create_repo().create_file.side_effect = GithubException(
            status=422, data=""
        )

        g = Github("abc123")
        org = dsegithub.organization.get_organization(g, "test")

        repository = dsegithub.repository.create_repository(org, "test-repo")
        self.assertFalse(dsegithub.repository.create_folder(repository, "test-folder"))

    @patch.object(Github, "get_organization")
    def test_create_folder_exists(self, mock_github):
        g = Github("abc123")
        org = dsegithub.organization.get_organization(g, "test")

        repository = dsegithub.repository.create_repository(org, "test-repo")
        self.assertFalse(dsegithub.repository.create_folder(repository, "test-folder"))

    @patch.object(Github, "get_user", autospec=True)
    @patch.object(Github, "get_organization")
    def test_add_user(self, mock_organization, mock_user):
        mock_organization().create_repo().add_to_collaborators.return_value = None

        g = Github("abc123")
        org = dsegithub.organization.get_organization(g, "test")

        repository = dsegithub.repository.create_repository(org, "test-repo")
        user = dsegithub.user.get_user(g, "test-user")
        self.assertIsNone(dsegithub.repository.add_user(repository, user))
