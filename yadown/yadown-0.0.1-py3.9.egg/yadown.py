import json
import signal
import requests
import subprocess
from urllib import parse
from urllib.parse import urlparse


API_URL = "https://cloud-api.yandex.net/v1/disk/public/resources/download"


def get_download_url(file_url):
    params = {
        "public_key": file_url, 
        "fields": "href"
    }
    response = requests.get(API_URL, params=params)
    json_response_content = response.content.decode()
    parsed_json = json.loads(json_response_content)
    download_url = parsed_json["href"]
    return download_url


def get_filename_from_url(url):
    parsed_url = urlparse(url)
    query = parsed_url.query
    query_dict = parse.parse_qs(query)
    filename = query_dict["filename"][0]
    return filename


def download(url):
    download_url = get_download_url(url)
    filename = get_filename_from_url(download_url)
    proc = subprocess.Popen(
        ["wget", f'{download_url}', "--progress=bar:force", "-O", filename], 
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
            proc.send_signal(signal.SIGINT)
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
    download_url = get_download_url(file_url)
    print(f"Download url: {download_url}")
    filename = get_filename_from_url(download_url)
    print(f"Filename: {filename}")


if __name__ == "__main__":
    main()
