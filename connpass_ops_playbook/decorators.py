from functools import wraps

import chromedriver_autoinstaller
from helium import start_chrome, start_firefox

from connpass_ops_playbook.playbooks import login_with_env


def using_firefox(func):
    """Firefoxを使うことを示すデコレータ

    Firefoxを空のページで立ち上げる

    注意：他のデコレータと一緒に使う場合、一番外側に置く必要がある（まずブラウザを立ち上げるため）
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_firefox()
        func(*args, **kwargs)

    return wrapper


def using_chrome(func):
    """Google Chromeを使うことを示すデコレータ

    Chromeを空のページで立ち上げる

    注意：他のデコレータと一緒に使う場合、一番外側に置く必要がある（まずブラウザを立ち上げるため）
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        chromedriver_autoinstaller.install()
        start_chrome()
        func(*args, **kwargs)

    return wrapper


def logged_in(func):
    """connpassにログインすることを示すデコレータ"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        login_with_env()
        func(*args, **kwargs)

    return wrapper
