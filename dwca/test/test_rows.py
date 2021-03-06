# -*- coding: utf-8 -*-

import unittest

from dwca.read import DwCAReader

from .helpers import BASIC_ARCHIVE_PATH, NOHEADERS1_PATH, MULTIEXTENSIONS_ARCHIVE_PATH


class TestCoreRow(unittest.TestCase):
    def test_position(self):
        # Test with archives with and without headers:
        archives_to_test = (BASIC_ARCHIVE_PATH, NOHEADERS1_PATH)

        for archive_path in archives_to_test:
            with DwCAReader(archive_path) as dwca:
                for i, row in enumerate(dwca):
                    self.assertEqual(i, row.position)


class TestExtensionRow(unittest.TestCase):
    def test_position(self):

        with DwCAReader(MULTIEXTENSIONS_ARCHIVE_PATH) as dwca:
            ostrich = dwca.rows[0]

            description_first_line = ostrich.extensions[0]
            description_second_line = ostrich.extensions[1]

            vernacular_first_line = ostrich.extensions[2]
            vernacular_second_line = ostrich.extensions[3]
            vernacular_third_line = ostrich.extensions[4]

            self.assertEqual (0, description_first_line.position)
            self.assertEqual(1, description_second_line.position)

            self.assertEqual(0, vernacular_first_line.position)
            self.assertEqual(1, vernacular_second_line.position)
            self.assertEqual(2, vernacular_third_line.position)