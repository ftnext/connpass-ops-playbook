import contextlib

from helium import kill_browser, start_firefox


@contextlib.contextmanager
def using_firefox():
    """Firefoxを使うコンテキストマネージャ

    例外が送出された場合にも kill_browser() し、ブラウザウィンドウが残らない
    """
    start_firefox()
    try:
        yield
    finally:
        kill_browser()
