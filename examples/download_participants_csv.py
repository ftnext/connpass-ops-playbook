"""Firefoxでconnpassにあるイベントから参加一覧CSVをダウンロードする作業を自動化"""

import argparse
import os
from pathlib import Path

from connpass_ops_playbook.decorators import (
    logged_in,
    using_firefox_with_options,
)
from connpass_ops_playbook.playbooks import download_latest_participants_csv
from helium import kill_browser
from selenium.webdriver import FirefoxOptions

options = FirefoxOptions()
options.set_preference("browser.download.useDownloadDir", True)
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", os.getcwd())
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")


@using_firefox_with_options(options)
@logged_in
def download(url):
    download_latest_participants_csv(url)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    args = parser.parse_args()

    download(args.url)

    print("download 終わり")
    print(list(Path(".").glob("*.csv")))

    kill_browser()
