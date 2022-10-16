import time
from datetime import datetime, timedelta
from typing import Optional

import requests
from bs4 import BeautifulSoup
from requests import Response


def retry_handle(username, year) -> Optional[Response]:
    retry_cnt = 0
    res = None

    while retry_cnt < 5:
        res = requests.get(f'https://github.com/users/{username}/contributions?to={year}-12-31')

        if res.status_code != 200:
            time.sleep(1)
            retry_cnt += 1
            continue

        break

    if retry_cnt >= 5:
        print('Requests Retry Limit')

    return res


def get_streak(username: str) -> (bool, int):
    """
    :param username: github username
    :return:
        - is_completed: Whether the crawl was successful
        - streak_count: streak commit count
    """
    now = datetime.now() - timedelta(days=1)  # check from the day before
    streak_count = 0
    is_commit_aborted = False
    is_completed = True

    for year in range(now.year, 2007, -1):  # GitHub opened in 2007
        time.sleep(0.1)  # 429 error prevention
        res = retry_handle(username, year)

        if not res:
            is_completed = False
            break

        soup = BeautifulSoup(res.text, "lxml")  # lxml faster than html.parse
        for rect in reversed(soup.select('rect')):
            if not rect.get('data-date') or now.date() < datetime.strptime(rect.get('data-date'), '%Y-%m-%d').date():
                continue

            if not rect.get('data-count') or rect.get('data-count') == '0':
                is_commit_aborted = True
                break

            streak_count += 1

        if is_commit_aborted:
            break

    return is_completed, streak_count
