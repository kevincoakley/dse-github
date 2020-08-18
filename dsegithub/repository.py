#!/usr/bin/env python

from github.GithubException import GithubException
from github.GithubException import UnknownObjectException


def get_repository(organization, repository_name):
    """
    Get GitHub Repository instance
    :param organization: GitHub Organization instance
    :param repository_name: name of the repository to get
    :return: GitHub Repository instance
    """

    try:
        return organization.get_repo(repository_name)
    except UnknownObjectException:
        return None


def create_repository(organization, repository_name):
    """
    Create GitHub Repository instance
    :param organization: GitHub Organization instance
    :param repository_name: name of the repository to create
    :return: GitHub Repository instance
    """
    try:
        return organization.create_repo(repository_name, private=True)
    except GithubException:
        return None
