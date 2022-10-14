import os
import json
import signal
import requests
import platform
import subprocess
from urllib import parse
from urllib.parse import urlparse
from urllib.parse import ParseResult
from typing import Union


API_URL = "https://cloud-api.yandex.net/v1/disk/public/resources/download"


def get_download_url(file_url: ParseResult) -> ParseResult:
    params = {
        "public_key": file_url.geturl(), 
        "fields": "href"
    }
    response = requests.get(API_URL, params=params)
    json_response_content = response.content.decode()
    parsed_json = json.loads(json_response_content)
    download_url = parsed_json["href"]
    return urlparse(download_url)


def get_filename_from_url(url: ParseResult):
    query = url.query
    query_dict = parse.parse_qs(query)
    filename = query_dict["filename"][0]
    return filename


def download(url: Union[ParseResult, str]):
    if isinstance(url, str):
        url = urlparse(url)
    download_url = get_download_url(url)
    filename = get_filename_from_url(download_url)
    proc = subprocess.Popen(
        ["wget", f'{download_url.geturl()}', "--progress=bar:force", "-O", filename], 
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    nl_counter = 0
    skip_lines_count = 8
    for _ in range(skip_lines_count):
        proc.stdout.readline()
    while True:
        try:
            wget_bytes = proc.stdout.readline(80)
        except KeyboardInterrupt:
            if platform.system() == "Linux":
                proc.send_signal(signal.SIGINT)
            else:
                os.kill(proc.pid, signal.CTRL_C_EVENT)
            break
        if len(wget_bytes) == 0: break
        if len(wget_bytes) == 1:
            if nl_counter == 1:
                print()
            nl_counter += 1
            continue
        line = wget_bytes.decode()
        print(line, end="")


def main():
    file_url = "https://disk.yandex.ru/d/P2p1tRpLlQIR1Q"
    print(f"File url: {file_url}")
    parsed_file_url = urlparse(file_url)
    download_url = get_download_url(parsed_file_url)
    print(f"Download url: {download_url}")
    filename = get_filename_from_url(download_url)
    print(f"Filename: {filename}")


if __name__ == "__main__":
    main()
