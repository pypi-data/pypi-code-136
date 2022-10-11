import datetime
from pathlib import Path

import typer
from dateutil.parser import parse
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

app = typer.Typer(name="twlib")


@app.command()
def hello(
    name: str,
    create_png: bool = typer.Option(False, help="create a png."),
    file: Path = typer.Argument(default=None, help="ultisnips source", exists=True),
):
    typer.echo(f"Hello {name}, {file}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")


@app.command()
def epoch2dt(
    epoch: int = typer.Argument(..., help="epoch in seconds"),
    to_local: bool = typer.Option(False, help="In local time"),
):
    if to_local:
        dt = datetime.datetime.fromtimestamp(epoch).strftime("%Y-%m-%d %H:%M:%S")
    else:
        dt = datetime.datetime.utcfromtimestamp(epoch).strftime("%Y-%m-%d %H:%M:%S")

    typer.echo(dt)


@app.command()
def dt2epoch(
    dt: str = typer.Argument(..., help="datetime string in '%Y-%m-%d %H:%M:%S'"),
    is_local: bool = typer.Option(False, help="Input is given in local time"),
):
    """Convert datetime string to epoch"""
    if is_local:
        # https://stackoverflow.com/a/39079819
        LOCAL_TIMEZONE = (
            datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
        )

        dt_parsed = parse(dt)  # get naive dt
        dt_parsed = dt_parsed.replace(tzinfo=LOCAL_TIMEZONE)  # localize naive dt
    else:
        dt_parsed = parse(dt)
        dt_parsed = dt_parsed.replace(tzinfo=datetime.timezone.utc)

    epoch = dt_parsed.timestamp()

    typer.echo(epoch)


def _convert_heif(input_file: str, mode: str, out_file: str | None) -> None:
    with Image.open(input_file) as img:
        print(
            f"{img.mode=}, {img.size=}, {img.format=}, {img.info.keys()=}, {img.getbands()=}"
        )

        if mode == "jpg":
            if out_file is None:
                out_file = Path(input_file).with_suffix(".jpg")
            Path(out_file).unlink(missing_ok=True)
            Path(out_file).parent.mkdir(parents=True, exist_ok=True)
            img.save(out_file, "JPEG")

        elif mode == "png":
            if out_file is None:
                out_file = Path(input_file).with_suffix(".png")
            Path(out_file).unlink(missing_ok=True)
            Path(out_file).parent.mkdir(parents=True, exist_ok=True)
            img.save(out_file, "PNG")
        else:
            raise ValueError(f"Unknown type {mode}")


@app.command()
def convert_heif(input_file: str, *, mode="jpg", out_file: str = None) -> None:
    _convert_heif(input_file=input_file, mode=mode, out_file=out_file)
    typer.echo(f"Saved {out_file}")


if __name__ == "__main__":
    app()
