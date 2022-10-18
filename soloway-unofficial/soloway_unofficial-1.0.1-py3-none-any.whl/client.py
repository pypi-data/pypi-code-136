import time

import requests
from tqdm import tqdm


class Client:
    HOST = "https://dsp.soloway.ru/api/"

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.x_sid: str | None = None
        self.account_info: dict | None = None
        self.placements: list[dict] | None = None
        self.placements_guid: list[str] | None = None
        self.guid: str | None = None
        self.report = None

    def login(self):
        params = {"username": self.username,
                  "password": self.password}
        time.sleep(1)
        resp = requests.post(f"{self.HOST}login", params=params)
        if resp.status_code != 200:
            raise ConnectionError(resp.text)
        self.x_sid = resp.headers.get("X-sid")

    def whoami(self):
        if not self.x_sid:
            print("Авторизация не пройдена")
            return
        headers = {"X-sid": self.x_sid}
        time.sleep(1)
        resp = requests.get(f"{self.HOST}whoami", headers=headers)
        if resp.status_code != 200:
            raise ConnectionError(resp.text)
        self.account_info = resp.json()
        self.guid = self.account_info['client']['guid']

    def get_placements(self):
        if not self.x_sid:
            self.login()
        if not self.guid:
            self.whoami()
        headers = self.__build_header()
        resp = requests.get(f"{self.HOST}clients/{self.guid}/placements", headers=headers)
        if resp.status_code != 200:
            raise ConnectionError(f"{resp.status_code}: {resp.text}")
        self.placements = resp.json()['list']
        self.__parse_placements_guid()

    def __parse_placements_guid(self):
        placements = [placement['doc']["guid"] for placement in tqdm(self.placements)]
        self.placements_guid = placements

    def get_placements_stat_all(self, start_date: str, stop_date: str, with_archived: bool = False) -> list[dict]:
        self.report = []
        if not self.x_sid:
            self.login()
        if not self.placements_guid:
            self.get_placements()
        return self.get_placements_stat(self.placements_guid, start_date, stop_date, with_archived=with_archived)

    def get_placements_stat(self, placement_ids: [str], start_date: str, stop_date: str,
                            with_archived: bool = False) -> list[dict]:
        if not self.x_sid:
            self.login()
        payload = {"placement_ids": placement_ids,
                   "start_date": start_date,
                   "stop_date": stop_date}
        if with_archived:
            payload["with_archived"] = 1
        headers = self.__build_header()
        time.sleep(1)
        resp = requests.get(f"{self.HOST}/api/placements_stat", json=payload, headers=headers)
        if resp.status_code != 200:
            raise ConnectionError(resp.text)
        return resp.json()

    def get_placement_stat_by_day(self, placement_guid: str, start_date: str, stop_date: str) -> dict | None:
        payload = {"start_date": start_date,
                   "stop_date": stop_date}
        headers = self.__build_header()
        time.sleep(1)
        resp = requests.post(f"{self.HOST}placements/{placement_guid}/stat", json=payload, headers=headers)
        if resp.status_code != 200:
            raise ConnectionError(resp.text)
        return resp.json()

    def get_placements_stat_by_day(self, start_date: str, stop_date: str) -> list[dict] | None:
        self.report = []
        if not self.placements:
            self.get_placements()
        report: list[dict] = []
        for placement in tqdm(self.placements_guid):
            data = self.get_placement_stat_by_day(placement, start_date, stop_date)
            report.append(data)
        logger.success("Данные собраны")
        self.report = report
        return self.report

    def __build_header(self):
        return {"Accept": "application/json",
                "Content-Type": "application/json",
                "X-sid": self.x_sid}
