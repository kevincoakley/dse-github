#!/usr/bin/env python

from github.GithubException import UnknownObjectException
import logging

logger = logging.getLogger("dse_github.user")


def get_user(g, name):
    """
    Get GitHub NamedUser instance
    :param g: GitHub instance
    :param name: name of the user to get
    :return: GitHub NamedUser instance
    """

    try:
        logger.debug("Getting User: %s" % name)
        user = g.get_user(name)
        logger.info("Found User: %s" % user.login)
        return user
    except UnknownObjectException:
        logger.info("User %s NOT found" % name)
        return None
