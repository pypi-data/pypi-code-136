class StockTrackerError(Exception):
    '''Root class to raise error'''

    pass


class CompanyNotFoundError(StockTrackerError):
    '''When user tries to get the company details that does
       not exists'''

    pass


class ConnectionError(StockTrackerError):
    '''When user tries to get the company details when user
       is not connected to internet'''

    pass
