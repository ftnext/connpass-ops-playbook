from unittest import TestCase
from unittest.mock import call, patch

from connpass_ops_playbook import plays


class LoginTestCase(TestCase):
    @patch("connpass_ops_playbook.plays.wait_until")
    @patch("connpass_ops_playbook.plays.Text")
    @patch("connpass_ops_playbook.plays.click")
    @patch("connpass_ops_playbook.plays.write")
    @patch("connpass_ops_playbook.plays.go_to")
    def test_login(self, go_to, write, click, Text, wait_until):
        username = "the_user"
        password = "pass123"

        plays.login(username, password)

        go_to.assert_called_once_with("connpass.com/login")
        write.assert_has_calls(
            [call(username, into="ユーザー名"), call(password, into="パスワード")]
        )
        click.assert_called_once_with("ログインする")
        Text.assert_called_once_with("あなたのイベント")
        wait_until.assert_called_once_with(Text.return_value.exists)
