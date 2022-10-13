from pylovepdf_flavor.task import Task


class Officetopdf(Task):

    def __init__(self, public_key, verify_ssl, proxies):

        self.tool = 'officetopdf'
        super(Officetopdf, self).__init__(public_key, True, verify_ssl, proxies)
