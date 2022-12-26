import os
import logging as log

import Constants


def create_directory(full_dir_path):
    log.info("In create_directory(full_dir_path) with Input values :" + full_dir_path)
    if not os.path.exists(full_dir_path):
        os.makedirs(full_dir_path)
        log.info("Created Directory : ", full_dir_path)
    else:
        log.info("Directory already existed : ", full_dir_path)


def create_supporting_folder():
    log.info("In create_supporting_folder()")
    if not os.path.exists(Constants.PARENT_DATA_DIR):
        os.mkdir(Constants.PARENT_DATA_DIR)

    if not os.path.exists(Constants.JSON_FILES_DIR):
        os.mkdir(Constants.JSON_FILES_DIR)

    if not os.path.exists(Constants.PDF_FILES_DIR):
        os.mkdir(Constants.PDF_FILES_DIR)

    if not os.path.exists(Constants.HTML_FILES_DIR):
        os.mkdir(Constants.HTML_FILES_DIR)

    if not os.path.exists(Constants.EPUB_FILES_DIR):
        os.mkdir(Constants.EPUB_FILES_DIR)
