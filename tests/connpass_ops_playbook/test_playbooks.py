from unittest import TestCase
from unittest.mock import call, patch

from connpass_ops_playbook import playbooks


class LoginWithEnvTestCase(TestCase):
    @patch("connpass_ops_playbook.playbooks.login")
    @patch("connpass_ops_playbook.playbooks.os.getenv")
    def test_login_success(self, getenv, login):
        getenv.side_effect = ["the_user", "pass123"]

        playbooks.login_with_env()

        getenv.assert_has_calls(
            [call("CONNPASS_USERNAME"), call("CONNPASS_PASSWORD")]
        )
        login.assert_called_once_with("the_user", "pass123")
