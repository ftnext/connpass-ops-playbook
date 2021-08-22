from unittest import TestCase

from connpass_ops_playbook import urls


class ToParticipantsManagementUrlTestCase(TestCase):
    def test_normal_event_url(self):
        event_url = "https://awesome-group.connpass.com/event/1234567/"
        expected = "https://connpass.com/event/1234567/participants/"

        actual = urls.to_participants_management_url(event_url)

        self.assertEqual(actual, expected)
