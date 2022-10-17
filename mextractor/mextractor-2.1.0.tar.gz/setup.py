# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mextractor']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'opencv-python>=4.6.0,<5.0.0',
 'pydantic-numpy>=1.3.0,<2.0.0',
 'pydantic>=1.9.2,<2.0.0',
 'ruamel.yaml>=0.17.21,<0.18.0',
 'setuptools']

extras_require = \
{':python_version >= "3.7" and python_version < "3.8"': ['numpy>=1.21.0,<2.0.0'],
 ':python_version >= "3.8" and python_version < "3.11"': ['numpy'],
 'video-extract': ['ffmpeg-python>=0.2.0,<0.3.0']}

entry_points = \
{'console_scripts': ['mextractor = mextractor.cli:mextractor_cli']}

setup_kwargs = {
    'name': 'mextractor',
    'version': '2.1.0',
    'description': 'mextractor can extract media metadata to YAML and read them',
    'long_description': '# mextractor: media metadata extractor\n\nVideos and images can be large. \n\n## Installation\n\nDownload and install from PyPi with `pip`:\n\n```shell\npip install mextractor\n```\nIf you are extracting metadata from videos, install additional dependencies:\n```shell\npip install mextractor[video-extract]\n```\n\n## Usage\nPlease back up your files before using them with the package, things might break during runtime causing corruption.\n\n### Command line interface (CLI)\n\nCopy directory to a new directory while extracting media info and a single frame from videos in subdirectories:\n```shell\nmextractor video-subdirs <path_to_root>\n```\n\n### Programmatically\nThese functions are useful when integrating mextractor to your own package. You can also use it for quick scripts, see the `mextractor.workflows` submodule for inspiration.\n\n#### Extract and dump metadata\n\n##### Video\n\n```python\nfrom mextractor.workflow import extract_and_dump_video\n\nmetadata = extract_and_dump_video(dump_dir, path_to_video, include_image, greyscale, lossy_compress_image)\n```\n\n##### Image\n\n```python\nfrom mextractor.workflow import extract_and_dump_image\n\nmetadata = extract_and_dump_image(dump_dir, path_to_image, include_image, greyscale, lossy_compress_image)\n```\n\n#### Load media\n\n##### Video\n\n```python\nimport mextractor\n\nvideo_metadata = mextractor.load(mextractor_dir)\n\nprint(video_metadata.average_fps)\nprint(video_metadata.frames)\nprint(video_metadata.resolution)\nprint(video_metadata.video_length_in_seconds)\n```\n\n##### Image\n\n```python\nimport mextractor\n\nimage_metadata = mextractor.load(mextractor_dir)\n\nprint(image_metadata.resolution)\n```\n',
    'author': 'Can H. Tartanoglu',
    'author_email': 'canhtart@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://pypi.org/project/mextractor/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
