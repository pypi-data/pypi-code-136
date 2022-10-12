from newrelic.nerdgraph.client import NerdGraphClient
from newrelic.synthetic.secure_credential import SecureCredential
from newrelic.synthetic.scripted_browser import ScriptedBrowserMonitors


class Synthetic:
    def __init__(self, client: NerdGraphClient) -> None:
        self.client = client
        self._secure_cred = None
        self._scripted_browser = None

    @property
    def secure_credential(self):
        if self._secure_cred is None:
            self._secure_cred = SecureCredential(client=self.client)
        return self._secure_cred

    @property
    def scripted_browser(self):
        if self._scripted_browser is None:
            self._scripted_browser = ScriptedBrowserMonitors(
                client=self.client
                )
        return self._scripted_browser
