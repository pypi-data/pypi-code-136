import logging
from concurrent.futures import ThreadPoolExecutor

from pyGuardPoint.guardpoint_dataclasses import Cardholder
from pyGuardPoint.guardpoint import GuardPoint, GuardPointError


class GuardPointAsync():

    def __init__(self, **kwargs):
        self.gp = GuardPoint(**kwargs)
        self.executor = ThreadPoolExecutor(max_workers=1)

    def get_card_holder(self, on_finished, uid):
        def handle_future(future):
            try:
                r = future.result()
                on_finished(r)
            except GuardPointError as e:
                on_finished(e)
            except Exception as e:
                on_finished(GuardPointError(e))

        future = self.executor.submit(self.gp.get_card_holder, uid)
        future.add_done_callback(handle_future)

    def get_card_holders(self, on_finished, offset=0, limit=10, searchPhrase=None):
        def handle_future(future):
            try:
                r = future.result()
                on_finished(r)
            except GuardPointError as e:
                on_finished(e)
            except Exception as e:
                on_finished(GuardPointError(e))

        future = self.executor.submit(self.gp.get_card_holders, offset, limit, searchPhrase)
        future.add_done_callback(handle_future)





if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    gp = GuardPointAsync(host="sensoraccess.duckdns.org", pwd="password")

    def task_complete(resp):
        if isinstance(resp, GuardPointError):
            print(f"Got back a GuardPointError: {resp}")
        if isinstance(resp, Cardholder):
            cardholder = resp
            print("Cardholder:")
            print("\tUID: " + cardholder.uid)
            print("\tFirstname: " + cardholder.firstName)
            print("\tLastname: " + cardholder.lastName)

        if isinstance(resp, list):
            cardholders = resp
            for cardholder in cardholders:
                print("Cardholder: ")
                print("\tUID: " + cardholder.uid)
                print("\tFirstname: " + cardholder.firstName)
                print("\tLastname: " + cardholder.lastName)

    try:
        gp.get_card_holder(task_complete, "422edea0-589d-4224-af0d-77ed8a97ca57")
        gp.get_card_holders(task_complete, searchPhrase="john")
        gp.get_card_holders(task_complete, searchPhrase="robert")
        gp.get_card_holders(task_complete, searchPhrase="josh")
        gp.get_card_holders(task_complete, searchPhrase="frida")
    except Exception as e:
        print(e)

    print("Got to End")
