from time import sleep

from .attack_base import BaseAttackMethod


"""
attack @ server, added by Shanshan, 07/04/2022
"""


class NetworkAttack(BaseAttackMethod):
    def __init__(self, args):
        self.network_delay = args.network_delay

    def delay_response(self):
        sleep(self.network_delay/1000.0)
