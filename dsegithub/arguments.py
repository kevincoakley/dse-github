#!/usr/bin/env python

import os
import argparse


def parse_arguments(args):
    """
    Parse Commandline Arguments
    :param args: *args positional arguments
    :return: Commandline arguments parsed by argparse
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("--debug", dest="debug", action="store_true")

    user_pass_group = parser.add_argument_group("group")

    user_pass_group.add_argument(
        "--username",
        metavar="username",
        dest="username",
        help="GitHub Username",
        default=os.environ.get("GITHUB_USERNAME", None),
    )

    user_pass_group.add_argument(
        "--password",
        metavar="password",
        dest="password",
        help="GitHub Password",
        default=os.environ.get("GITHUB_PASSWORD", None),
    )

    parser.add_argument(
        "--access-token",
        metavar="access_token",
        dest="access_token",
        help="GitHub Access Token",
        default=os.environ.get("ACCESS_TOKEN", None),
    )

    parser.add_argument(
        "--org",
        metavar="organization",
        dest="organization",
        help="GitHub Organization",
        required=True,
        default=os.environ.get("GITHUB_ORGANIZATION", None),
    )

    parser.add_argument(
        "--file",
        metavar="file",
        dest="file",
        help="CSV file with GitHub Username and Repository",
        required=True,
        default=os.environ.get("CSV_FILE", None),
    )

    # Verify username, password and access_token are not all None
    if (
        parser.parse_args(args).username is None
        and parser.parse_args(args).password is None
        and parser.parse_args(args).access_token is None
    ):
        parser.error("Username and Password or Access Token are required.")

    # Verify if username or password is specified then both username and
    # password are specified
    if (
        parser.parse_args(args).username is not None
        or parser.parse_args(args).password is not None
    ):
        if (
            parser.parse_args(args).username is None
            or parser.parse_args(args).password is None
        ):
            parser.error("Username and Password are BOTH required.")

    return parser.parse_args(args)
