import os

from connpass_ops_playbook.plays import login


def login_with_env():
    if not (username := os.getenv("CONNPASS_USERNAME")):
        raise RuntimeError("Set environment variable `CONNPASS_USERNAME`")
    password = os.getenv("CONNPASS_PASSWORD")
    login(username, password)
