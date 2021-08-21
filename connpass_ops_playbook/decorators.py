from functools import wraps

from helium import start_firefox


def using_firefox(func):
    """Firefoxを使うことを示すデコレータ

    Firefoxを空のページで立ち上げる
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_firefox()
        func(*args, **kwargs)

    return wrapper
