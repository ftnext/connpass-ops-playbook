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


@patch("connpass_ops_playbook.plays.wait_until")
@patch("connpass_ops_playbook.plays.Text")
@patch("connpass_ops_playbook.plays.Alert")
@patch("connpass_ops_playbook.plays.click")
@patch("connpass_ops_playbook.plays.go_to")
class CopyExistingEventTestCase(TestCase):
    def setUp(self):
        self.url = "https://awesome-group.connpass.com/event/1234567/"

    def test_copy(self, go_to, click, Alert, Text, wait_until):
        plays.copy_existing_event(self.url)

        go_to.assert_called_once_with(self.url)
        click.assert_called_once_with("コピーを作成")
        Alert.assert_called_once_with()
        Alert.return_value.accept.assert_called_once_with()
        Text.assert_called_once_with("下書き中")
        wait_until.assert_called_once_with(Text.return_value.exists)

    def test_human_confirm_is_true(
        self, go_to, click, Alert, Text, wait_until
    ):
        plays.copy_existing_event(self.url, human_confirms=True)

        go_to.assert_called_once_with(self.url)
        click.assert_called_once_with("コピーを作成")
        Alert.assert_not_called()
        Text.assert_not_called()
        wait_until.assert_not_called()


class DownloadParticipantsCsvTestCase(TestCase):
    @patch("connpass_ops_playbook.plays.wait_until")
    @patch("connpass_ops_playbook.plays.Path")
    @patch("connpass_ops_playbook.plays.click")
    @patch("connpass_ops_playbook.plays.go_to")
    def test_download(self, go_to, click, Path, wait_until):
        url = "https://connpass.com/event/1234567/participants/"
        csv_path = "event_1234567_participants.csv"

        plays.download_participants_csv(url, csv_path)

        go_to.assert_called_once_with(url)
        click.assert_called_once_with("CSVダウンロード")
        Path.assert_called_once_with(csv_path)
        wait_until.assert_called_once_with(Path.return_value.exists)
