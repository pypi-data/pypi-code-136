import re
import argparse
from urllib.parse import urlparse
from yadown import download


def yandex_url(arg):
    url = urlparse(arg)
    if not all([url.scheme, url.netloc, url.path]) or not url.scheme.startswith("http"):
        raise argparse.ArgumentTypeError("Invalid URL")
    if not (url.netloc == "disk.yandex.ru" or url.netloc == "yadi.sk"):
        raise argparse.ArgumentTypeError("Not a yandex disk URL")
    if not re.match("^/d/[a-zA-Z0-9]{14}$", url.path):
        raise argparse.ArgumentTypeError("Invalid path")
    return url


def run():
    parser = argparse.ArgumentParser(description="Download files from Я.Диск")
    parser.add_argument("url", help="Link to file or folder in Я.Диск", metavar="url", type=yandex_url)
    args = parser.parse_args()
    download(args.url)


if __name__ == "__main__":
    run()
