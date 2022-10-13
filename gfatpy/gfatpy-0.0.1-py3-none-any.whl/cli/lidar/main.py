import pathlib
from datetime import datetime
from typing import Optional
from pathlib import Path

import typer

from gfatpy.lidar.types import LidarName, MeasurementType
from gfatpy.lidar.raw2l1.lidar_raw2l1 import lidar_raw2l1
from gfatpy.lidar.reader import reader_xarray
from gfatpy.lidar.quality_assurance.rayleigh_fit import rayleigh_fit_from_date

app = typer.Typer(no_args_is_help=True)


@app.command(
    help="Converts raw lidar data to l1 data",
    no_args_is_help=True,
)
def raw2l1(
    lidar_name: LidarName = typer.Option(..., "--lidar", "-l"),
    initial_date: datetime = typer.Option(..., "--initial-date", "-i"),
    data_dir: Path = typer.Option(
        ..., "--data-dir", "-d", readable=True, dir_okay=True, file_okay=False
    ),
    measurement_type: MeasurementType = typer.Option(
        MeasurementType.RS, "--measurement-type", "-t"
    ),
    final_date: Optional[datetime] = typer.Option(None, "--final-date", "-f"),
    overwrite: bool = typer.Option(False, "--overwrite", "-w"),
):
    lidar_raw2l1(
        lidar_name,
        data_dir,
        measurement_type,
        initial_date,
        final_date,
        overwrite,
    )


@app.command(no_args_is_help=True)
def plot(
    lidar_name: LidarName = typer.Option(..., "--lidar", "-l"),
    initial_date: datetime = typer.Option(..., "--initial-date", "-i"),
    final_date: Optional[datetime] = typer.Option(None, "--final-date", "-f"),
):
    typer.echo(f"{lidar_name}")
    typer.echo(f"{initial_date}")
    typer.echo(f"{final_date}")


@app.command(no_args_is_help=True)
def reader(
    filelist: pathlib.Path = typer.Option(..., "--file-list", "-f"),
    initial_date: datetime = typer.Option(..., "--initial-date", "-i"),
    final_date: Optional[datetime] = typer.Option(None, "--final-date", "-f"),
    initial_range: Optional[float] = typer.Option(0.0, "--initial-range", "-g"),
    final_range: Optional[float] = typer.Option(30000.0, "--final-range", "-t"),
    percentage_required: Optional[float] = typer.Option(
        80.0, "--percentage-required", "-p"
    ),
    _channels: Optional[str] = typer.Option([], "--channels", "-c"),
):
    channels = _channels.split(",")

    typer.echo(f"{filelist}")
    typer.echo(f"{initial_date}")
    typer.echo(f"{final_date}")
    typer.echo(f"{initial_range}")
    typer.echo(f"{final_range}")
    typer.echo(f"{percentage_required}")
    typer.echo(f"{channels}")

    reader_xarray(
        filelist,
        date_ini=initial_date,
        date_end=final_date,
        ini_range=initial_range,
        end_range=final_range,
        percentage_required=percentage_required,
        channels=channels,
    )


@app.command(help="QA Rayleigh fit", no_args_is_help=True)
def rayleigh_fit(
    initial_date: datetime = typer.Option(..., "--initial-date", "-i"),
    lidar_name: LidarName = typer.Option(..., "--lidar", "-l"),
    data_dir: Path = typer.Option(
        ..., "--data-dir", "-d", readable=True, dir_okay=True, file_okay=False
    ),
    output_dir: Path = typer.Option(
        ...,
        "--output-dir",
        "-o",
        readable=True,
        writable=True,
        dir_okay=True,
        file_okay=False,
    ),
    channels: str = typer.Option(..., "--channels", "-c"),
):
    channels_list = channels.split(",")
    assert len(channels_list) > 0, "At least one channel is required"

    rayleigh_fit_from_date(
        date=initial_date,
        channels=channels_list,
        lidar_name=lidar_name.value,
        data_dir=data_dir,
        output_dir=output_dir,
        save_fig=True,
    )
