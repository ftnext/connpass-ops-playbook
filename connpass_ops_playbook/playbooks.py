import os
from pathlib import Path

from send2trash import send2trash

from connpass_ops_playbook.plays import download_participants_csv, login
from connpass_ops_playbook.urls import search_event_id


def login_with_env():
    if not (username := os.getenv("CONNPASS_USERNAME")):
        raise RuntimeError("Set environment variable `CONNPASS_USERNAME`")
    if not (password := os.getenv("CONNPASS_PASSWORD")):
        raise RuntimeError("Set environment variable `CONNPASS_PASSWORD`")
    login(username, password)


def download_latest_participants_csv(url):
    event_id = search_event_id(url)
    if not event_id:
        raise ValueError(f"Specified URL does not include event id: {url}")

    participants_management_url = (
        f"https://connpass.com/event/{event_id}/participants/"
    )
    csv_path = f"event_{event_id}_participants.csv"
    if Path(csv_path).exists():
        # 最新のCSVファイルだけを残すため、すでにあるファイルはゴミ箱へ移す
        send2trash(csv_path)

    download_participants_csv(participants_management_url, csv_path)
