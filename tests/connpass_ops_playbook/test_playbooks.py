from unittest import TestCase
from unittest.mock import call, patch

from connpass_ops_playbook import playbooks


@patch("connpass_ops_playbook.playbooks.login")
@patch("connpass_ops_playbook.playbooks.os.getenv")
class LoginWithEnvTestCase(TestCase):
    def test_login_success(self, getenv, login):
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
