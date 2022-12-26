import os
from unittest import TestCase

import Constants
import Utils


class TestUtils(TestCase):

    def test_create_directory(self):
        if os.path.exists("./TEST_FOLDER"):
            os.removedirs("./TEST_FOLDER")
        Utils.create_directory("./TEST_FOLDER")
        self.assertEqual(os.path.exists("./TEST_FOLDER"), True)

    def test_create_folder(self):
        Utils.create_supporting_folder()
        self.assertEqual(os.path.exists(Constants.PARENT_DATA_DIR), True)
        self.assertEqual(os.path.exists(Constants.JSON_FILES_DIR), True)
        self.assertEqual(os.path.exists(Constants.PDF_FILES_DIR), True)
        self.assertEqual(os.path.exists(Constants.HTML_FILES_DIR), True)
        self.assertEqual(os.path.exists(Constants.EPUB_FILES_DIR), True)
