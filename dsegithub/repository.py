#!/usr/bin/env python

from github.GithubException import GithubException
from github.GithubException import UnknownObjectException
import logging

logger = logging.getLogger("dse_github.repository")


def get_repository(organization, repository_name):
    """
    Get GitHub Repository instance
    :param organization: GitHub Organization instance
    :param repository_name: name of the repository to get
    :return: GitHub Repository instance
    """

    try:
        logger.debug("Getting repository: %s" % repository_name)
        repository = organization.get_repo(repository_name)
        logger.info("Repository found: %s", repository.name)
        return repository
    except UnknownObjectException:
        logger.info("Repository NOT found: %s", repository_name)
        return None


def create_repository(organization, repository_name):
    """
    Create GitHub Repository instance
    :param organization: GitHub Organization instance
    :param repository_name: name of the repository to create
    :return: GitHub Repository instance
    """

    try:
        logger.debug("Creating repository: %s" % repository_name)
        repository = organization.create_repo(repository_name, private=True)
        logger.info("Repository created: %s", repository.name)
        return repository
    except GithubException:
        logger.info("Repository NOT created: %s", repository_name)
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
        logger.debug("Checking if README.md exists in %s" % repository.name)
        repository.get_readme()
        logger.info("README.md exists in %s" % repository.name)
    except UnknownObjectException:
        try:
            # Only create the README.md if one doesn't exist
            logger.debug("Creating README.md in %s" % repository.name)
            repository.create_file("README.md", message, content)
            logger.info("README.md created in %s" % repository.name)
            return True
        except GithubException:
            logger.info("README.md NOT created in %s" % repository.name)
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
        logger.debug("Checking if folder %s exists in %s" % (folder, repository.name))
        repository.get_contents("%s/README.md" % folder)
        logger.info("Folder %s exists in %s" % (folder, repository.name))
    except UnknownObjectException:
        try:
            # Only create folder/README.md if it doesn't exist
            logger.debug("Creating folder %s in %s" % (folder, repository.name))
            repository.create_file("%s/README.md" % folder, message, content)
            logger.info("Folder %s created in %s" % (folder, repository.name))
            return True
        except GithubException:
            logger.info("Folder %s NOT created in %s" % (folder, repository.name))
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

    logger.info(
        "Adding User %s to Repository %s (%s)"
        % (user.login, repository.name, permission)
    )
    return repository.add_to_collaborators(user, permission)
