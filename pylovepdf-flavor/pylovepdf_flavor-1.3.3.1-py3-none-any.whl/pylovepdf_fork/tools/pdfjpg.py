from pylovepdf_flavor.task import Task


class PdfJpg(Task):

    def __init__(self, public_key, verify_ssl, proxies):

        self.pdfjpg_mode = 'pages'

        self.tool = 'pdfjpg'
        super(PdfJpg, self).__init__(public_key, True, verify_ssl, proxies)

    @property
    def allowed_properties(self):
        return 'pdfjpg_mode',

    @property
    def pdfjpg_mode_values(self):
        return 'pages', 'extract'

    def process(self):

        payload = super(PdfJpg, self).process()
        payload = self.as_dict(payload, self.allowed_properties)

        return payload






