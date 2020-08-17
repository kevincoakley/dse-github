#!/usr/bin/env python


def create_get_team(organization, team_name):
    """
    Create and Get GitHub Team
    :param organization: GitHub Organization instance
    :param team_name: name of the team to create and get
    :return: GitHub Team instance
    """

    for team in organization.get_teams():
        if team.name == team_name:
            return team

    return organization.create_team(team_name)
