from unittest import TestCase
from unittest.mock import patch

from connpass_ops_playbook import decorators as d


@patch("connpass_ops_playbook.decorators.start_firefox")
class UsingFirefoxTestCase(TestCase):
    def test_without_parenthesis(self, start_firefox):
        @d.using_firefox
        def f():
            ...

        f()

        start_firefox.assert_called_once_with()

    def test_with_parenthesis(self, start_firefox):
        @d.using_firefox()
        def f():
            ...

        f()

        start_firefox.assert_called_once_with()


class UsingChromeTestCase(TestCase):
    @patch("connpass_ops_playbook.decorators.start_chrome")
    @patch("connpass_ops_playbook.decorators.chromedriver_autoinstaller")
    def test_start_chrome(self, chromedriver_autoinstaller, start_chrome):
        @d.using_chrome
        def f():
            ...

        f()

        chromedriver_autoinstaller.install.assert_called_once_with()
        start_chrome.assert_called_once_with()


class LoggedInTestCase(TestCase):
    @patch("connpass_ops_playbook.decorators.login_with_env")
    def test_logged_in(self, login_with_env):
        @d.logged_in
        def f():
            ...

        f()

        login_with_env.assert_called_once_with()
