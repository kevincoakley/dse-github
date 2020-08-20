#!/usr/bin/env python

from github.GithubException import UnknownObjectException


def get_user(g, name):
    """
    Get GitHub NamedUser instance
    :param g: GitHub instance
    :param name: name of the user to get
    :return: GitHub NamedUser instance
    """

    try:
        return g.get_user(name)
    except UnknownObjectException:
        return None
