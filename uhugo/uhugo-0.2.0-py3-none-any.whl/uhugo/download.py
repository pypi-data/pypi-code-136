import os.path
import platform
import tempfile

import requests
from rich.progress import Progress, TextColumn, BarColumn, DownloadColumn, TransferSpeedColumn, \
    TimeRemainingColumn

progress = Progress(
    TextColumn("[bold blue]{task.fields[filename]}", justify="right"),
    BarColumn(),
    "[progress.percentage]{task.percentage:>3.1f}%",
    "•",
    DownloadColumn(),
    "•",
    TransferSpeedColumn(),
    "•",
    TimeRemainingColumn(),
    transient=True
)


def download_hugo_zip(version: str, os_type: str = None, download_to: str = None) -> str:
    """
    Download the Hugo file to temp folder.

    :param os_type: OS type
    :param version: Version number to download
    :param download_to: Path to download to
    """

    if not os_type:
        os_type = platform.system()

    if not download_to:
        download_to = tempfile.gettempdir()

    download_to = os.path.join(download_to, f"hugo_{version}")
    with progress:
        task_id = progress.add_task("download", filename=f"hugo_{version}", start=False)

        with open(download_to, "wb") as file:
            if os_type == 'Darwin':
                response = requests.get(
                    f"https://github.com/gohugoio/hugo/releases/download/v{version}/hugo_extended_{version}_darwin-universal.tar.gz",
                    stream=True)
            elif os_type == 'Windows' or os_type == 'nt':
                response = requests.get(
                    f"https://github.com/gohugoio/hugo/releases/download/v{version}/hugo_extended_{version}_windows-amd64.zip",
                    stream=True)
            elif os_type == "posix" or os_type == "Linux":
                response = requests.get(
                    f"https://github.com/gohugoio/hugo/releases/download/v{version}/hugo_extended_{version}_linux-amd64.zip",
                    stream=True)
            else:
                raise OSError(f"{os_type} not supported.")

            if response.headers.get('Status') == "404 Not Found":
                raise requests.exceptions.HTTPError("File not found")

            total_length = int(response.headers.get('content-length'))

            if total_length is None:
                progress.console.print(f"- Downloading Hugo v{version}")
                file.write(response.content)
                progress.update(task_id, completed=True)
                progress.console.print("- Hugo downloaded")
            else:
                progress.console.print(f"- Downloading Hugo v{version}")
                progress.update(task_id, total=total_length)
                progress.start_task(task_id)
                for data in response.iter_content(chunk_size=4096):
                    file.write(data)
                    progress.update(task_id, advance=len(data))
                progress.console.print("- Hugo downloaded")

    return download_to
