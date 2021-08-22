from unittest import TestCase
from unittest.mock import call, patch

from connpass_ops_playbook import playbooks


@patch("connpass_ops_playbook.playbooks.login")
@patch("connpass_ops_playbook.playbooks.os.getenv")
class LoginWithEnvTestCase(TestCase):
    def test_when_env_vars_are_set(self, getenv, login):
        getenv.side_effect = ["the_user", "pass123"]

        playbooks.login_with_env()

        getenv.assert_has_calls(
            [call("CONNPASS_USERNAME"), call("CONNPASS_PASSWORD")]
        )
        login.assert_called_once_with("the_user", "pass123")

    def test_error_when_username_unset(self, getenv, login):
        getenv.return_value = None

        with self.assertRaises(RuntimeError) as cm:
            playbooks.login_with_env()

        self.assertEqual(
            str(cm.exception), "Set environment variable `CONNPASS_USERNAME`"
        )
        getenv.assert_called_once_with("CONNPASS_USERNAME")
        login.assert_not_called()

    def test_error_when_password_unset(self, getenv, login):
        getenv.side_effect = ["the_user", None]

        with self.assertRaises(RuntimeError) as cm:
            playbooks.login_with_env()

        self.assertEqual(
            str(cm.exception), "Set environment variable `CONNPASS_PASSWORD`"
        )
        getenv.assert_has_calls(
            [call("CONNPASS_USERNAME"), call("CONNPASS_PASSWORD")]
        )
        login.assert_not_called()


@patch("connpass_ops_playbook.playbooks.download_participants_csv")
@patch("connpass_ops_playbook.playbooks.search_event_id")
class DownloadLatestParticipantsCsvTestCase(TestCase):
    def test_valid_url(self, search_event_id, download_participants_csv):
        url = "https://awesome-group.connpass.com/event/1234567/"
        search_event_id.return_value = 1234567

        participants_management_url = (
            "https://connpass.com/event/1234567/participants/"
        )
        csv_path = "event_1234567_participants.csv"

        playbooks.download_latest_participants_csv(url)

        search_event_id.assert_called_once_with(url)
        download_participants_csv.assert_called_once_with(
            participants_management_url, csv_path
        )

    def test_raise_error_when_invalid_url(
        self, search_event_id, download_participants_csv
    ):
        url = "https://connpass.com/login"
        search_event_id.return_value = None

        with self.assertRaises(ValueError) as cm:
            playbooks.download_latest_participants_csv(url)

        self.assertEqual(
            str(cm.exception),
            "Specified URL does not include event id: "
            "https://connpass.com/login",
        )
        search_event_id.assert_called_once_with(url)
        download_participants_csv.assert_not_called()
