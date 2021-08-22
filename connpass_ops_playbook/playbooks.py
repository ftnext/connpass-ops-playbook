import os

from connpass_ops_playbook.plays import download_participants_csv, login
from connpass_ops_playbook.urls import search_event_id


def login_with_env():
    if not (username := os.getenv("CONNPASS_USERNAME")):
        raise RuntimeError("Set environment variable `CONNPASS_USERNAME`")
    if not (password := os.getenv("CONNPASS_PASSWORD")):
        raise RuntimeError("Set environment variable `CONNPASS_PASSWORD`")
    login(username, password)


def download_latest_participants_csv(url):
    raise NotImplementedError
