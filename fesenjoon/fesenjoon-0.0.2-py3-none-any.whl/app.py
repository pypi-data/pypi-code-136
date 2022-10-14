from argparse import ArgumentParser
from os import getenv
from pathlib import Path

from Drive import Drive

path_download_required = False
path_download = Path(getenv("PATH_DOWNLOAD"))

if not path_download.exists():
    path_download.mkdir(parents=True)

parser = ArgumentParser(description="URL of file or folder")

# parser.add_argument("-u", "--url", help="URL", type=str, default=None, required=True)
parser.add_argument("-u", "--url", help="URL", type=str, default=None)

parser.add_argument("-d", "--depth-level", help="Depth", type=str, default="0")
parser.add_argument("-o", "--out", help="Out", type=str, default=path_download)
parser.add_argument("-mi", "--mimetype-include", help="Depth", type=str, default="all")
parser.add_argument("-me", "--mimetype-exclude", help="Depth", type=str, default=None)

parser.add_argument("-up", "--upload-dir", help="UPLOAD DIR", type=str)


args = parser.parse_args()
url = args.url
depth = int(args.depth_level)
out = Path(args.out)
# path_upload = Path(args.upload_dir)


if not out.exists():
    out.mkdir(parents=True)

drive = Drive()
# print(depth)
drive.download(url, depth, out)

# print(drive.upload_dir(path_upload))

# files_generator = drive.download_memory(url)

# for i, file in enumerate(files_generator):
#     with open(f"x{i}", "wb") as f:
#         f.write(file)
