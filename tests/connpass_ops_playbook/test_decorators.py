from unittest import TestCase
from unittest.mock import patch

from connpass_ops_playbook import decorators as d


class UsingFirefoxTestCase(TestCase):
    @patch("connpass_ops_playbook.decorators.start_firefox")
    def test_start_firefox(self, start_firefox):
        @d.using_firefox
        def f():
            ...

        f()

        start_firefox.assert_called_once_with()


class LoggedInTestCase(TestCase):
    @patch("connpass_ops_playbook.decorators.login_with_env")
    def test_logged_in(self, login_with_env):
        @d.logged_in
        def f():
            ...

        f()

        login_with_env.assert_called_once_with()
