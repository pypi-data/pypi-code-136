import click
from code_size_analyzer_client.client_wrapper import ClientWrapper
from code_size_analyzer_client.api_client import ApiClient
import json
from otel_extensions import (
    init_telemetry_provider,
    TelemetryOptions,
    flush_telemetry_data,
)
from retry import retry
import logging


@click.command()
@click.option("--map_file", required=True, help="path to map file")
@click.option(
    "--stack_name", required=True, help="stack owner name (i.e. zigbee, matter)"
)
@click.option(
    "--target_part", required=True, help="target part (e.g. efr32mg22c224f512im40)"
)
@click.option("--compiler", required=True, help="compiler name (gcc or iar)")
@click.option("--project_file", default=None, help="path to project file")
@click.option(
    "--service_url",
    default="https://code-size-analyzer.silabs.net",
    help="service endpoint",
)
@click.option(
    "--output_file",
    default=None,
    help="path to output json file (default is to stdout)",
)
@click.option("--verify_ssl", default=True, help="verify ssl certificate on server")
@click.option("--target_board", default=None, help="target board (e.g. brd4181a)")
@click.option("--app_name", default=None, help="application name")
@click.option("--branch_name", default=None, help="branch name")
@click.option("--build_number", default=None, help="build number")
@click.option("--store_results", default=False, help="store results to database")
@click.option(
    "--uc_component_branch_name",
    default=None,
    help="branch name for uc component-based categorization (e.g. use develop/22q4 for a feature branch branched off develop/22q4)",
)
def main(
    map_file,
    stack_name,
    target_part,
    compiler,
    project_file,
    service_url,
    output_file,
    verify_ssl,
    target_board,
    app_name,
    branch_name,
    build_number,
    store_results,
    uc_component_branch_name,
):
    logging.getLogger("opentelemetry.util._time").setLevel(logging.ERROR)
    init_telemetry_provider(
        TelemetryOptions(
            OTEL_SERVICE_NAME="Code Size Analyzer CLI",
        )
    )
    client_wrapper = ClientWrapper(server_url=service_url, verify_ssl=verify_ssl)

    @retry(tries=6, delay=1, max_delay=10, backoff=2)
    def call_analyzer():
        r = client_wrapper.analyze_map_file(
            map_file,
            stack_name,
            target_part,
            compiler,
            project_file,
            target_board=target_board,
            app_name=app_name,
            branch_name=branch_name,
            build_number=build_number,
            store_results=store_results,
            uc_component_branch_name=uc_component_branch_name,
        )
        j = json.dumps(ApiClient.sanitize_for_serialization(r), indent=2)
        if output_file is not None:
            with open(output_file, "w") as f:
                f.write(j)
        else:
            print(j)

    call_analyzer()
    flush_telemetry_data()


if __name__ == "__main__":
    main()
