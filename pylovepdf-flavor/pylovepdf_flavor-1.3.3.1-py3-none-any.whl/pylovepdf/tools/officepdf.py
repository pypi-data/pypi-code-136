from pylovepdf.task import Task


class OfficePdf(Task):

    def __init__(self, public_key, verify_ssl, proxies):

        self.tool = 'officepdf'
        super(OfficePdf, self).__init__(public_key, True, verify_ssl, proxies)
