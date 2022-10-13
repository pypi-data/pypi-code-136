import unittest
from mock import Mock, patch

from otrs_somconnexio.services.unblock_mobile_pack_ticket import \
    UnblockMobilePackTicket


class UnblockMobilePackTicketTestCase(unittest.TestCase):

    @patch('otrs_somconnexio.services.unblock_mobile_pack_ticket.OTRSClient',
       return_value=Mock(spec=[
           'update_ticket',
           'get_ticket_by_number',
        ])
    )
    @patch('otrs_somconnexio.services.unblock_mobile_pack_ticket.DynamicField')
    def test_run(self, MockDF, MockOTRSClient):
        ticket_number = "123"
        expected_df = [object()]
        MockDF.return_value = expected_df
        MockOTRSClient.return_value.get_ticket_by_number.return_value = Mock(spec=['id'])
        MockOTRSClient.return_value.get_ticket_by_number.return_value.id = 321

        UnblockMobilePackTicket(ticket_number).run()

        MockOTRSClient.return_value.get_ticket_by_number.assert_called_once_with(
            ticket_number
        )
        MockOTRSClient.return_value.update_ticket.assert_called_once_with(
            MockOTRSClient.return_value.get_ticket_by_number.return_value.id,
            article=None,
            dynamic_fields=[expected_df]
        )
        MockDF.assert_called_once_with(
            name='DynamicField_recuperarProvisio',
            value=1,
        )
