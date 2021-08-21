from helium import Text, click, wait_until, write


def login(username, password):
    """ユーザー名とパスワードを入力してログインする

    前提：ブラウザはログイン画面に遷移している

    画面参考
    https://help.connpass.com/basic/login.html
    """
    write(username, into="ユーザー名")
    write(password, into="パスワード")
    click("ログインする")

    wait_until(Text("あなたのイベント").exists)
