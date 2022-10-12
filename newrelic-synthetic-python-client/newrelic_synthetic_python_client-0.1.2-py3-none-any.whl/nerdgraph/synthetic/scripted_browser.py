from typing import List, Literal


class Graphql:
    @staticmethod
    def list() -> str:
        return """{
            actor {
                entitySearch(query: "domain = 'SYNTH' AND type = 'MONITOR'") {
                results {
                    entities {
                    ... on SyntheticMonitorEntityOutline {
                        guid
                        name
                        accountId
                        monitorType
                        tags {
                        key
                        values
                        }
                    }
                    }
                }
                }
            }
            }
        """

    @staticmethod
    def add(
        account_id: str,
        locations: List[str],
        monitor_name: str,
        period: str,
        script_content: str,
        status: Literal["ENABLED", "DISABLED", "MUTED"],
        enable_screenshot: Literal["true", "false"]
    ) -> str:
        valid_periods = [
            "EVERY_MINUTE",
            "EVERY_5_MINUTES",
            "EVERY_10_MINUTES",
            "EVERY_15_MINUTES",
            "EVERY_30_MINUTES",
            "EVERY_HOUR",
            "EVERY_6_HOURS",
            "EVERY_12_HOURS",
            "EVERY_DAY",
        ]
        assert period in valid_periods, (
            f"Value of period: {period} is not valid, "
            f"valid periods are {valid_periods}"
        )
        valid_status = ["ENABLED", "DISABLED", "MUTED"]
        assert status in valid_status, (
            f"Value of status: {status} is not valid,"
            f"valid status are {valid_status}."
        )
        return """
            mutation {
                syntheticsCreateScriptBrowserMonitor (
                accountId: """ + account_id + """,
                monitor: {
                    locations: {
                    public: [""" + ','.join([f'"{x}"' for x in locations]) + """]
                    },
                    name: \"""" + monitor_name + """\",
                    period: """ + period + """,
                    runtime: {
                    runtimeType: "CHROME_BROWSER",
                    runtimeTypeVersion: "100",
                    scriptLanguage: "JAVASCRIPT"
                    }
                    script: \"""" + script_content + """\",
                    status: """ + status + """,
                    advancedOptions: {
                    enableScreenshotOnFailureAndScript: """ + enable_screenshot + """
                    }
                }
                ) {
                errors {
                    description
                    type
                }
                }
            }
    """

    @staticmethod
    def update(
        guid: str,
        locations: List[str],
        monitor_name: str,
        period: str,
        script_content: str,
        status: Literal["ENABLED", "DISABLED", "MUTED"],
        enable_screenshot: Literal["true", "false"]
    ) -> str:
        valid_periods = [
            "EVERY_MINUTE",
            "EVERY_5_MINUTES",
            "EVERY_10_MINUTES",
            "EVERY_15_MINUTES",
            "EVERY_30_MINUTES",
            "EVERY_HOUR",
            "EVERY_6_HOURS",
            "EVERY_12_HOURS",
            "EVERY_DAY",
        ]
        assert period in valid_periods, (
            f"Value of period: {period} is not valid, "
            f"valid periods are {valid_periods}"
        )
        valid_status = ["ENABLED", "DISABLED", "MUTED"]
        assert status in valid_status, (
            f"Value of status: {status} is not valid,"
            f"valid status are {valid_status}."
        )
        return """
        mutation {
            syntheticsUpdateScriptBrowserMonitor (
            guid: \"""" + guid + """\",
            monitor: {
                locations: {
                    public: [""" + ','.join([f'"{x}"' for x in locations]) + """]
                    },
                    name: \"""" + monitor_name + """\",
                    period: """ + period + """,
                    runtime: {
                    runtimeType: "CHROME_BROWSER",
                    runtimeTypeVersion: "100",
                    scriptLanguage: "JAVASCRIPT"
                    }
                    script: \"""" + script_content + """\",
                    status: """ + status + """,
                    advancedOptions: {
                    enableScreenshotOnFailureAndScript: """ + enable_screenshot + """
                    }
            }
            ) {
            errors {
                description
                type
            }
            }
        }
        """

    @staticmethod
    def get_script(account_id: str, guid: str):
        return """
    {
    actor {
        account(id: """ + account_id + """) {
        synthetics {
            script(monitorGuid: \"""" + guid + """\") {
            text
            }
        }
        }
    }
    }
    """
