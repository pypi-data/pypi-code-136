from pathlib import Path
from typing import Optional

import typer

from kiss_icp.datasets import (
    available_dataloaders,
    sequence_dataloaders,
    supported_file_extensions,
)


def name_callback(value: str):
    dl = available_dataloaders()
    if value not in dl:
        raise typer.BadParameter(f"Supported dataloaders are:\n{', '.join(dl)}")
    return value


def get_package_dir() -> str:
    import kiss_icp
    import os

    return os.path.dirname(kiss_icp.__file__)


app = typer.Typer(add_completion=False, rich_markup_mode="rich")

# Remove the clutter for the help
_available_dl_help = available_dataloaders()
_available_dl_help.remove("rosbag")
_available_dl_help.remove("generic")

docstring = f"""
:kiss: KISS-ICP, a simple yet effective LiDAR-Odometry estimation pipeline :kiss:\n
\b
[bold green]Examples: [/bold green]
# Process all pointclouds in the given <data-dir> \[{", ".join(supported_file_extensions())}]
$ kiss_icp_pipeline --visualize <data-dir>:open_file_folder:

# Process a given rosbag file
$ kiss_icp_pipeline --topic /cloud_node --visualize <path-to-my-rosbag.bag>:page_facing_up:

# Use a more specific dataloader: {", ".join(_available_dl_help)}
$ kiss_icp_pipeline --dataloader kitti --sequence 07 --visualize <path-to-kitti-root>:open_file_folder:
"""


@app.command(help=docstring)
def kiss_icp_pipeline(
    data: Path = typer.Argument(
        ...,
        help="The data directory used by the specified dataloader",
        show_default=False,
    ),
    dataloader: str = typer.Option(
        "generic",
        show_default=False,
        case_sensitive=False,
        autocompletion=available_dataloaders,
        callback=name_callback,
        help="[Optional] Use a specific dataloader from those supported by KISS-ICP",
    ),
    config: Path = typer.Option(
        f"{get_package_dir()}/config/default.yaml",
        "--config",
        exists=True,
        show_default=False,
        help="[Optional] Path to the configuration file",
    ),
    max_range: Optional[float] = typer.Option(
        None,
        "--max_range",
        show_default=False,
        help="[Optional] Overrides the max_range from the default configuration",
    ),
    deskew: bool = typer.Option(
        False,
        "--deskew",
        help="[Optional] Wheter or not to deskew the scan or not",
        show_default=False,
        is_flag=True,
    ),
    no_cache: Optional[bool] = typer.Option(
        None,
        "--no-cache",
        show_default=False,
        help="[Optional] Overrides the cache setup from the default configuration",
        is_flag=True,
    ),
    # Aditional Options ---------------------------------------------------------------------------
    visualize: bool = typer.Option(
        False,
        "--visualize",
        "-v",
        help="[Optional] Open an online visualization of the KISS-ICP pipeline",
        rich_help_panel="Additional Options",
    ),
    sequence: Optional[int] = typer.Option(
        None,
        "--sequence",
        "-s",
        show_default=False,
        help="[Optional] For some dataloaders, you need to specify a given sequence",
        rich_help_panel="Additional Options",
    ),
    topic: Optional[str] = typer.Option(
        None,
        "--topic",
        "-t",
        show_default=False,
        help="[Optional] Only valid when processing rosbag files",
        rich_help_panel="Additional Options",
    ),
    n_scans: int = typer.Option(
        -1,
        "--n-scans",
        "-n",
        show_default=False,
        help="[Optional] Specify the number of scans to process, default is the entire dataset",
        rich_help_panel="Additional Options",
    ),
    jump: int = typer.Option(
        0,
        "--jump",
        "-j",
        show_default=False,
        help="[Optional] Specify if you want to start to process scans from a given starting point",
        rich_help_panel="Additional Options",
    ),
):
    # Validate some options
    if dataloader in sequence_dataloaders() and sequence is None:
        print('You must specify a sequence "--sequence"')
        raise typer.Exit(code=1)

    # Check if the main source is a bagfile, then automatically fallback to RosbagDataset
    dataloader = "rosbag" if data.is_file() and data.name.split(".")[-1] == "bag" else dataloader

    # Lazy-loading for faster CLI
    from kiss_icp.datasets import dataset_factory
    from kiss_icp.pipeline import OdometryPipeline

    OdometryPipeline(
        dataset=dataset_factory(
            dataloader=dataloader,
            data_dir=data,
            config=config,
            # Additional options
            max_range=max_range,
            sequence=sequence,
            topic=topic,
            no_cache=no_cache,
        ),
        config=config,
        deskew=deskew,
        visualize=visualize,
        n_scans=n_scans,
        jump=jump,
    ).run()


def run():
    app()
