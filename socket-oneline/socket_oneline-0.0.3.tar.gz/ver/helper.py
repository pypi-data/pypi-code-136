import time

from ver.core.ver_services import VerServices


# -------------------
class Helper:

    # -------------------
    @staticmethod
    def wait_until_started(timeout):
        start_time = time.time()
        while (time.time() - start_time) < timeout:
            if VerServices.server.ols.is_running:
                break
            time.sleep(0.250)

    # -------------------
    @staticmethod
    def wait_until_stopped(timeout):
        start_time = time.time()
        while (time.time() - start_time) < timeout:
            if not VerServices.server.ols.is_running:
                break
            time.sleep(0.250)
