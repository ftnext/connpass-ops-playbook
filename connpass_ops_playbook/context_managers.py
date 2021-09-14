import contextlib

from helium import kill_browser, start_firefox


@contextlib.contextmanager
def using_firefox():
    start_firefox()
    yield
    kill_browser()
