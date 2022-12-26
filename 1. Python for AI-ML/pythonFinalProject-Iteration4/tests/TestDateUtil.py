from datetime import date
from unittest import TestCase
import DateUtil


class TestDateUtil(TestCase):

    def test_without_date(self):
        answer = DateUtil.get_date_YYYYMMDD(None)
        today = date.today()
        current_date = today.strftime("%Y%m%d")
        self.assertEqual(answer, current_date)

    def test_with_date(self):
        answer = DateUtil.get_date_YYYYMMDD("20220901")
        self.assertEqual(answer, "20220901")
