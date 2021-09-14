from unittest import TestCase
from unittest.mock import patch

from connpass_ops_playbook import context_managers as cm


@patch("connpass_ops_playbook.context_managers.kill_browser")
@patch("connpass_ops_playbook.context_managers.start_firefox")
class UsingFirefoxTestCase(TestCase):
    def test_context_manager(self, start_firefox, kill_browser):
        with cm.using_firefox():
            ...

        start_firefox.assert_called_once_with()
        kill_browser.assert_called_once_with()

    def test_error_raises(self, start_firefox, kill_browser):
        with self.assertRaises(LookupError):  # 例外によりテストが落ちないようにする
            with cm.using_firefox():
                raise LookupError

        start_firefox.assert_called_once_with()
        kill_browser.assert_called_once_with()
