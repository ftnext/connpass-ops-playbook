"""Firefoxでconnpassにある既存のイベントをコピーするまでを自動化"""

import argparse

from connpass_ops_playbook.decorators import logged_in, using_firefox
from connpass_ops_playbook.plays import copy_existing_event
from helium import kill_browser


@using_firefox
@logged_in
def show_copy_popup(url):
    copy_existing_event(url, human_confirms=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    args = parser.parse_args()

    show_copy_popup(args.url)

    while True:
        user_input = input("qで終了: ")
        cleaned_input = user_input.rstrip().lower()
        if cleaned_input == "q":
            kill_browser()
            break
