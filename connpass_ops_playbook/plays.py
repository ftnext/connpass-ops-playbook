from helium import Text, click, go_to, wait_until, write


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
