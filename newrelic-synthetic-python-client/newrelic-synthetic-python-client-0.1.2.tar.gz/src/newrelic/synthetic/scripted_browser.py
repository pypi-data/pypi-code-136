from typing import Dict, List, Literal

from newrelic.utils.log import log
from newrelic.nerdgraph.client import NewRelicModule
import newrelic.nerdgraph.synthetic.scripted_browser \
    as scripted_browser


class ScriptedBrowserMonitors(NewRelicModule):
    def list(self) -> Dict:
        graphql = scripted_browser.Graphql.list()
        r = self.client.request(ql=graphql)
        return r.json()

    def find_by_name(self, monitor_name) -> Dict:
        monitors = self.list()
        search = filter(
            lambda x: x["name"] == monitor_name,
            monitors["data"]["actor"]["entitySearch"]["results"]["entities"]
            )
        return next(search)

    def add(
        self,
        locations: List[str],
        monitor_name: str,
        period: str,
        script_content: str,
        status: Literal["ENABLED", "DISABLED", "MUTED"],
        enable_screenshot: Literal["true", "false"]
    ) -> Dict:
        graphql = scripted_browser.Graphql.add(
            account_id=self.client.account_id,
            locations=locations,
            monitor_name=monitor_name,
            period=period,
            script_content=script_content,
            status=status,
            enable_screenshot=enable_screenshot
        )
        r = self.client.request(ql=graphql)
        return r.json()

    def update(
        self,
        monitor_name: str,
        locations: List[str],
        period: str,
        script_content: str,
        status: Literal["ENABLED", "DISABLED", "MUTED"],
        enable_screenshot: Literal["true", "false"]
    ) -> Dict:
        monitor = self.find_by_name(monitor_name=monitor_name)
        graphql = scripted_browser.Graphql.update(
            monitor_name=monitor_name,
            guid=monitor["guid"],
            locations=locations,
            period=period,
            script_content=script_content,
            status=status,
            enable_screenshot=enable_screenshot
        )
        r = self.client.request(ql=graphql)
        return r.json()

    def get_script(self, monitor_name: str, **kwargs) -> Dict:
        monitor = self.find_by_name(monitor_name=monitor_name)
        graphql = scripted_browser.Graphql.get_script(
            account_id=self.client.account_id,
            guid=monitor["guid"]
        )
        r = self.client.request(ql=graphql)
        return r.json()

    def put(
        self,
        monitor_name: str,
        locations: List[str],
        period: str,
        script_content: str,
        status: Literal["ENABLED", "DISABLED", "MUTED"],
        enable_screenshot: Literal["true", "false"]
    ) -> Dict:
        r = self.list()
        log.debug("Got list of scripted browser monitors successfully")
        results = r["data"]["actor"]["entitySearch"]["results"]["entities"]
        log.trace(f"List of scripted browser monitors: {results}")
        if monitor_name in [x["name"] for x in results]:
            log.info(f"Monitor {monitor_name} exists, updating the monitor")
            return self.update(
                monitor_name=monitor_name,
                locations=locations,
                period=period,
                script_content=script_content,
                status=status,
                enable_screenshot=enable_screenshot
                )
        log.info(
            f"Monitor {monitor_name} does not exist, create a new monitor"
            )
        return self.add(
            monitor_name=monitor_name,
            locations=locations,
            period=period,
            script_content=script_content,
            status=status,
            enable_screenshot=enable_screenshot
            )
