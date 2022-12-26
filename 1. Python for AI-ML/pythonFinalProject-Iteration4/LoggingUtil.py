import logging
import sys


# This method is used to enable logging at console level
def enable_logging_stdout():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(fmt='%(asctime)s {%(filename)s:%(funcName)s:%(lineno)d} %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    root.addHandler(handler)
    logging.info("enable_logging_stdout: Logging is Enabled at DEBUG level to display logs in STDOUT")
