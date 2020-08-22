#!/usr/bin/env python

import csv
import logging
import sys

logger = logging.getLogger("dse_github.csv")


def read_csv(file_path):
    """
    Read CSV File and Return
    :param file_path: the path and file of the csv file
    :return: list of dicts with the contents of the file_path
    """

    try:
        logger.debug("Reading %s" % file_path)
        with open(file_path, newline="") as csv_file:
            csv_data = csv.DictReader(csv_file)
            csv_list = list(csv_data)
            logger.info("Read %s line from %s" % (len(csv_list), file_path))
            return csv_list
    except FileNotFoundError:
        sys.exit("%s not found!" % file_path)
