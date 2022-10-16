from datetime import datetime

import requests

from .exceptions import (
    CannotBookClass,
    NoCreditAvailable,
    NoMoreOfTheSameClass,
    ProbablyInWaitList,
    SignInError,
)


class Client:
    BOOK_URL = "https://aimharder.com/api/book"
    BOOKINGS_URL = "https://aimharder.com/api/bookings"
    SIGNIN_URL = "https://aimharder.com/login"

    def __init__(self, mail: str, password: str, box_id: int) -> None:
        self.session = self._login(mail, password)
        self.box_id = box_id

    @staticmethod
    def _login(mail: str, password: str):
        session = requests.Session()
        response = session.post(
            Client.SIGNIN_URL,
            data={
                "loginiframe": 0,
                "mail": mail,
                "pw": password,
                "login": "Iniciar sesión",
            },
        )
        if response.status_code == 200 and response.history:
            return session
        else:
            raise SignInError()

    def bookings(self, day: datetime):
        response = self.session.get(
            Client.BOOKINGS_URL,
            params={
                "box": self.box_id,
                "day": day.strftime("%Y%m%d"),
                "familyId": "",
            },
        )
        return response.json()

    def book(self, day: datetime, class_id: str):
        response = self.session.post(
            Client.BOOK_URL,
            data={
                "id": class_id,
                "day": day.strftime("%Y%m%d"),
                "insist": 0,
                "familyId": "",
            },
        )

        if response.status_code != 200 or response.get("bookState") != 1:
            # Something wrong happened
            if response.get("bookState") == 0:
                raise ProbablyInWaitList()
            elif response.get("bookState") == -2:
                raise NoCreditAvailable()
            elif response.get("bookState") == -8:
                raise NoMoreOfTheSameClass(response.get("max"))
            else:
                raise CannotBookClass()
        else:
            return response.json()
