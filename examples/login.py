"""Firefoxでconnpassにログインするまでを自動化"""

from connpass_ops_playbook.decorators import using_firefox
from connpass_ops_playbook.playbooks import login_with_env
from helium import kill_browser

login_with_env = using_firefox(login_with_env)


if __name__ == "__main__":
    login_with_env()

    while True:
        user_input = input("qで終了: ")
        cleaned_input = user_input.rstrip().lower()
        if cleaned_input == "q":
            kill_browser()
            break
