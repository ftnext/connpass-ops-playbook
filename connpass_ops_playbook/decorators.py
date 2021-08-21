from functools import wraps

from helium import start_firefox

from connpass_ops_playbook.playbooks import login_with_env


def using_firefox(func):
    """Firefoxを使うことを示すデコレータ

    Firefoxを空のページで立ち上げる
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_firefox()
        func(*args, **kwargs)

    return wrapper


def logged_in(func):
    """connpassにログインすることを示すデコレータ"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        login_with_env()
        func(*args, **kwargs)

    return wrapper
