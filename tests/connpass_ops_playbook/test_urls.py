from unittest import TestCase

from connpass_ops_playbook import urls


class SearchEventId(TestCase):
    def test_normal_event_url(self):
        event_url = "https://awesome-group.connpass.com/event/1234567/"
        expected = 1234567

        actual = urls.search_event_id(event_url)

        self.assertEqual(actual, expected)

    def test_group_includes_numbers(self):
        event_url = "https://event2019.connpass.com/event/2345678/"
        expected = 2345678

        actual = urls.search_event_id(event_url)

        self.assertEqual(actual, expected)

    def test_numbers_not_included(self):
        event_url = "https://connpass.com/login"

        actual = urls.search_event_id(event_url)

        self.assertIsNone(actual)
