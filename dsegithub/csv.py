#!/usr/bin/env python

import csv
import sys


def read_csv(file_path):
    """
    Read CSV File and Return
    :param file_path: the path and file of the csv file
    :return: list of dicts with the contents of the file_path
    """

    try:
        with open(file_path, newline="") as csv_file:
            csv_data = csv.DictReader(csv_file)
            return list(csv_data)
    except FileNotFoundError:
        sys.exit("%s not found!" % file_path)
