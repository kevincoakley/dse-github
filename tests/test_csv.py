#!/usr/bin/env python

from mock import patch
import dsegithub.csv
import unittest


class CsvTestCase(unittest.TestCase):
    def setUp(self):
        pass

    @patch("csv.DictReader")
    def test_csv(self, mock_csv_reader):
        mock_csv_reader.return_value = [{"test": "value1"}, {"test": "value2"}]

        csv_out = dsegithub.csv.read_csv("/Users/kcoakley/Downloads/form.csv")
        self.assertIsInstance(csv_out, list)
        self.assertIsInstance(csv_out[0], dict)

    def test_file_not_found(self):
        with self.assertRaises(SystemExit) as se:
            dsegithub.csv.read_csv("file_not_found.csv")
        self.assertEqual(se.exception.code, "file_not_found.csv not found!")
