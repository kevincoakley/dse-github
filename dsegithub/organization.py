#!/usr/bin/env python

from github.GithubException import BadCredentialsException
from github.GithubException import UnknownObjectException
import logging
import sys

logger = logging.getLogger("dse_github.organization")


def get_organization(g, organization_name):
    """
    Get GitHub Organization instance
    :param g: GitHub instance
    :param organization_name: name of the organization to get
    :return: GitHub Organization instance
    """

    try:
        logger.debug("Looking up Organization: %s" % organization_name)
        organization = g.get_organization(organization_name)
        logger.debug("Found Organization: %s" % organization.name)
    except BadCredentialsException:
        sys.exit("Invalid GitHub Credentials!")
    except UnknownObjectException:
        sys.exit("Organization %s not found!" % organization_name)

    return organization
