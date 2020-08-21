#!/usr/bin/env python

import sys
import logging
import dsegithub.arguments
import dsegithub.csv
import dsegithub.organization
import dsegithub.repository
import dsegithub.team
import dsegithub.user
from github import Github


def main():
    """
    :return: 0 if successful otherwise return an error message as a string
    """
    args = dsegithub.arguments.parse_arguments(sys.argv[1:])

    log_level = logging.INFO

    if args.debug is True:
        log_level = logging.DEBUG

    logger = logging.getLogger("dse_github")
    logger.setLevel(level=log_level)
    log_handler = logging.StreamHandler()
    log_formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(message)s"
    )
    log_handler.setFormatter(log_formatter)
    logger.addHandler(log_handler)

    if args.access_token is not None:
        # or using an access token
        g = Github(args.access_token)
    else:
        # using username and password
        g = Github(args.username, args.password)

    csv_repositories = dsegithub.csv.read_csv(args.file)

    # Get the MAS-DSE Organization
    organization = dsegithub.organization.get_organization(g, "mas-dse")

    # Loop through the csv file lines
    for csv_repository in csv_repositories:
        # Check if the repository exists
        repository = dsegithub.repository.get_repository(
            organization, csv_repository["Repository"]
        )

        # If the repository doesn't exist, then create it
        if repository is None:
            repository = dsegithub.repository.create_repository(
                organization, csv_repository["Repository"]
            )

        # Get the Instructor and TA GitHub Team Instances
        instructor_team = dsegithub.team.create_get_team(organization, "Instructors")
        ta_team = dsegithub.team.create_get_team(organization, csv_repository["Cohort"])

        # Add the Instructor and TA GitHub Teams to the Repository
        dsegithub.team.add_repository(instructor_team, repository)
        dsegithub.team.add_repository(ta_team, repository)

        # Create README.md file
        dsegithub.repository.create_readme(repository)

        # Create Course Folders
        course_folders = ["DSE200", "DSE210", "DSE201", "DSE220", "DSE230", "DSE203"]
        for folder in course_folders:
            dsegithub.repository.create_folder(repository, folder)

        # Get the User
        user = dsegithub.user.get_user(g, csv_repository["Username"])

        # If User Exists, Add User to the Repository
        if user is not None:
            # Add User to Repo
            dsegithub.repository.add_user(repository, user)

    return 0
