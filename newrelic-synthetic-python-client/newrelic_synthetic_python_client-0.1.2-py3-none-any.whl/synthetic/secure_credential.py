from typing import Dict

from newrelic.utils.log import log
from newrelic.nerdgraph.client import NewRelicModule
import newrelic.nerdgraph.synthetic.secure_credential as secure_credential


class SecureCredential(NewRelicModule):
    def list(self) -> Dict:
        graphql = secure_credential.Graphql.list()
        resp = self.client.request(ql=graphql)
        return resp.json()

    def update(
        self,
        key: str,
        value: str,
        description: str,
    ) -> Dict:
        graphql = secure_credential.Graphql.update(
            account_id=self.client.account_id,
            key=key,
            value=value,
            description=description
        )
        r = self.client.request(
            ql=graphql
            )
        return r.json()

    def add(
        self,
        key: str,
        value: str,
        description: str,
    ) -> Dict:
        graphql = secure_credential.Graphql.add(
            account_id=self.client.account_id,
            key=key,
            value=value,
            description=description
        )
        r = self.client.request(
            ql=graphql
            )
        return r.json()

    def put(
        self,
        key: str,
        value: str,
        description: str,
    ) -> Dict:
        r = self.list()
        log.debug("Got list of credentials successfully")
        results = r["data"]["actor"]["entitySearch"]["results"]["entities"]
        log.trace(f"List of credentials: {results}")
        if key in [x["name"] for x in results]:
            log.info(f"Key {key} exists, updating the credential")
            return self.update(key=key, value=value, description=description)
        log.info(f"Key {key} does not exist, create a new credential")
        return self.add(key=key, value=value, description=description)
