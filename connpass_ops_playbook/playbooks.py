import os

from connpass_ops_playbook.plays import login


def login_with_env():
    username = os.getenv("CONNPASS_USERNAME")
    password = os.getenv("CONNPASS_PASSWORD")
    login(username, password)
