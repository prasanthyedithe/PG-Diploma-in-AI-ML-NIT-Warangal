from unittest import TestCase

import RSSFeedSupport
import RSSFeedUtil


class TestRSSFeedUtil(TestCase):

    def setUp(self) -> None:
        self.entry = RSSFeedSupport.fetch_rss_feed("https://news.yahoo.com/rss/").entries

    def test_print_all_feeds(self):
        RSSFeedUtil.print_all_feeds(self.entry)
        self.assertGreater(len(self.entry[1].title), 1)

    def test_print_range_feeds(self):
        RSSFeedUtil.print_range_feeds(self.entry, 1)
        self.assertGreater(len(self.entry[1].title), 1)

    def test_construct_json_all_feeds(self):
        output_list = RSSFeedUtil.construct_json_all_feeds(self.entry, my_json_list=[])
        self.assertGreater(len(output_list), 1)

    def test_construct_json_range_feeds(self):
        output_list = RSSFeedUtil.construct_json_range_feeds(self.entry, 1, my_json_list=[])
        self.assertEqual(len(output_list), 1)
