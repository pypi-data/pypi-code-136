import requests
from .command_base import CliCommand


class ReportCommand(CliCommand):
    @staticmethod
    def help():
        return 'Download a diagnostic report from your Auterion device'

    def __init__(self, config):
        self._sysinfo_api_endpoint = f"http://{config['device_address']}/api/sysinfo/v1.0"

    def setup_parser(self, parser):
        pass

    def run(self, args):
        report_name = "/tmp/report.zip"
        if len(args) > 2:
            if args[2] in ["-o", "--output"]:
                report_name = args[3]
        if not report_name.endswith(".zip"):
            report_name += ".zip"
        print(f"Downloading report: {report_name}")
        r = requests.get(f"{self._sysinfo_api_endpoint}/report")
        open(report_name, 'wb').write(r.content)
