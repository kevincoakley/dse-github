#!/usr/bin/env python

import logging

logger = logging.getLogger("dse_github.team")


def create_get_team(organization, team_name):
    """
    Create and Get GitHub Team
    :param organization: GitHub Organization instance
    :param team_name: name of the team to create and get
    :return: GitHub Team instance
    """

    logger.debug("Getting Team: %s" % team_name)
    for team in organization.get_teams():
        if team.name == team_name:
            logger.info("Found Team: %s" % team.name)
            return team

    logger.debug("Team not found, creating team: %s" % team_name)
    team = organization.create_team(team_name)
    logger.info("Created Team: %s" % team.name)
    return team


def add_repository(team, repository):
    """
    Added GitHub Repository to GitHub Team
    :param team: GitHub Team instance
    :param repository: GitHub Repository instance
    :return: None
    """

    logger.info("Adding Repository %s to Team %s" % (repository.name, team.name))
    return team.add_to_repos(repository)
