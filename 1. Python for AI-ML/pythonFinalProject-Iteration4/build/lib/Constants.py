import os
import pdfkit

PARENT_DATA_DIR = "data/"
JSON_FILES_DIR = PARENT_DATA_DIR + "JSON_FILES/"
PDF_FILES_DIR = PARENT_DATA_DIR + "PDF_FILES/"
HTML_FILES_DIR = PARENT_DATA_DIR + "HTML_FILES/"
EPUB_FILES_DIR = PARENT_DATA_DIR + "EPUB_FILES/"
TEMP_FILE = 'temp.txt'

MAX_RETRIES = 10  # Amount of Network-Error based request retries

FILE_EXTENSION_JSON = ".json"

CURRENT_WORKING_DIR = os.path.dirname(os.path.realpath(__file__))

# TODO : hard coded the wkhtmltopdf.ext file path
PDFKIT_CONFIG = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
