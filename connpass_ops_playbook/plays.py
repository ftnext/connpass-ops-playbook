from helium import Alert, Text, click, go_to, wait_until, write


def login(username, password):
    """ログイン画面に遷移し、ユーザー名とパスワードを入力してログインする

    画面参考
    https://help.connpass.com/basic/login.html
    """
    go_to("connpass.com/login")
    write(username, into="ユーザー名")
    write(password, into="パスワード")
    click("ログインする")

    wait_until(Text("あなたのイベント").exists)


def copy_existing_event(url):
    """指定したイベントをコピーする

    connpassの仕様上、管理者のイベントのみコピーできる

    画面参考（コピーを作成）
    https://help.connpass.com/organizers/event-detail.html#id32
    """
    go_to(url)
    click("コピーを作成")
    Alert().accept()

    wait_until(Text("下書き中").exists)
