# coding: utf-8
from pyotrs.lib import DynamicField

from otrs_somconnexio.client import OTRSClient


class UnblockMobilePackTicket:
    """
    Unblock the mobile pack tickets.

    Once the fiber provisioning is closed, we can start with the mobile provisioning to complete
    the pack products.
    Unblock is to change the DynamicField_recuperarProvisio to 1
    """

    def __init__(self, ticket_number):
        self.ticket_number = ticket_number

    def run(self):
        otrs_client = OTRSClient()
        ticket = otrs_client.get_ticket_by_number(self.ticket_number)

        dynamic_fields = [
            DynamicField(name='DynamicField_recuperarProvisio', value=1),
        ]
        otrs_client.update_ticket(
            ticket.id,
            article=None,
            dynamic_fields=dynamic_fields
        )
