import requests
from .command_base import CliCommand


class ReportCommand(CliCommand):
    @staticmethod
    def help():
        return 'Download a diagnostic report from your Auterion device'

    def __init__(self, config):
        self._sysinfo_api_endpoint = f"http://{config['device_address']}/api/sysinfo/v1.0"

    def setup_parser(self, parser):
        parser.add_argument('-o', '--output', help='output path of the diagnostic report', default='report.zip')

    def run(self, args):
        report_name = args.output
        if not report_name.endswith(".zip"):
            report_name += ".zip"
        print(f"Downloading report to {report_name}")
        r = requests.get(f"{self._sysinfo_api_endpoint}/report")
        open(report_name, 'wb').write(r.content)
