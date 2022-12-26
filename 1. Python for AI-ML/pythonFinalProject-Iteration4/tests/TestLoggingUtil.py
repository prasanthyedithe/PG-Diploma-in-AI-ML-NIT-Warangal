from unittest import TestCase
import LoggingUtil


class TestLoggingUtil(TestCase):

    def test_enable_logging_stdout(self):
        LoggingUtil.enable_logging_stdout()
