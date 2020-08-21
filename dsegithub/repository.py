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


def create_readme(repository):
    """
    Create README.md file for the Repository
    :param repository: GitHub Repository instance
    :return: True if README.md was created, otherwise False
    """

    message = "Added welcome message to README.md"
    content = (
        "%s\n========\n\nThis is your MAS-DSE Private GitHub Repository.\n\n"
        "A directory has been created for each course.\n\n"
        "See [https://mas-dse.github.io/startup/](https://mas-dse.github.io/startup/) "
        "for startup instructions." % repository.name
    )

    try:
        # Check if README.md exists
        repository.get_readme()
    except UnknownObjectException:
        try:
            # Only create the README.md if one doesn't exist
            repository.create_file("README.md", message, content)
            return True
        except GithubException:
            return False

    return False


def create_folder(repository, folder):
    """
    Create folder/README.md for the Repository
    :param repository: GitHub Repository instance
    :param folder: Name of the folder to create
    :return: True if README.md was created, otherwise False
    """

    message = "Created %s/README.md" % folder
    content = "%s\n======\n\nCourse directory for %s" % (folder, folder)

    try:
        # Check if folder/README.md exists
        repository.get_contents("%s/README.md" % folder)
    except UnknownObjectException:
        try:
            # Only create folder/README.md if it doesn't exist
            repository.create_file("%s/README.md" % folder, message, content)
            return True
        except GithubException:
            return False

    return False


def add_user(repository, user, permission="push"):
    """
    Grant User access to the Repository
    :param repository: GitHub Repository instance
    :param user: GitHub User instance
    :param permission: "pull", "push" or "admin"
    :return: None
    """

    return repository.add_to_collaborators(user, permission)
