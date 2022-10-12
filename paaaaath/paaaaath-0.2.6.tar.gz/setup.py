# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['paaaaath']

package_data = \
{'': ['*']}

install_requires = \
['smart-open>=5.0,<6.0']

extras_require = \
{':python_version >= "3.7" and python_version < "3.8"': ['importlib_metadata>=3.7,<4.0'],
 'all': ['boto3>=1.17.36,<2.0.0',
         'google-cloud-storage>=1.36.2,<2.0.0',
         'requests>=2.25.1,<3.0.0'],
 'gcs': ['google-cloud-storage>=1.36.2,<2.0.0'],
 'http': ['requests>=2.25.1,<3.0.0'],
 's3': ['boto3>=1.17.36,<2.0.0']}

setup_kwargs = {
    'name': 'paaaaath',
    'version': '0.2.6',
    'description': 'a useful alternative Path object',
    'long_description': '[![Build][build-shiled]][build-url]\n[![Version][version-shield]][version-url]\n[![Downloads][download-shield]][download-url]\n[![Contributors][contributors-shield]][contributors-url]\n[![Forks][forks-shield]][forks-url]\n[![Stargazers][stars-shield]][stars-url]\n[![Issues][issues-shield]][issues-url]\n[![MIT License][license-shield]][license-url]\n\n\n\n\n## About The Project\n\nThis project is motivated to provide a useful alternative Path object.\n\n### Built With\n\n- [poetry](https://python-poetry.org/)\n\n## Getting Started\n\n```sh\n$ pip install paaaaath\n$ python -c "from paaaaath import Path; print(Path(\'https://raw.githubusercontent.com/ar90n/paaaaath/main/assets/python_logo.txt\').read_text())"\n                   _.gj8888888lkoz.,_\n                d888888888888888888888b,\n               j88P""V8888888888888888888\n               888    8888888888888888888\n               888baed8888888888888888888\n               88888888888888888888888888\n                            8888888888888\n    ,ad8888888888888888888888888888888888  888888be,\n   d8888888888888888888888888888888888888  888888888b,\n  d88888888888888888888888888888888888888  8888888888b,\n j888888888888888888888888888888888888888  88888888888p,\nj888888888888888888888888888888888888888\'  8888888888888\n8888888888888888888888888888888888888^"   ,8888888888888\n88888888888888^\'                        .d88888888888888\n8888888888888"   .a8888888888888888888888888888888888888\n8888888888888  ,888888888888888888888888888888888888888^\n^888888888888  888888888888888888888888888888888888888^\n V88888888888  88888888888888888888888888888888888888Y\n  V8888888888  8888888888888888888888888888888888888Y\n   `"^8888888  8888888888888888888888888888888888^"\'\n               8888888888888\n               88888888888888888888888888\n               8888888888888888888P""V888\n               8888888888888888888    888\n               8888888888888888888baed88V\n                `^888888888888888888888^\n                  `\'"^^V888888888V^^\'\n```\n\n### Prerequisites\n\nIf you rune some codes in this repository, you have to install poetry as following.\n\n```sh\npip install poetry\n```\n\n### Installation\n\n```sh\npip install paaaaath\n```\n\n## Usage\n\n```python\nfrom paaaaath import Path\n\nOUTPUT_BUCKET = ""  # fill output bucket name\n\n\ndef main():\n    png_images = []\n    for p in Path("s3://elevation-tiles-prod/normal/10/963").iterdir():\n        if p.suffix != ".png":\n            continue\n\n        png_images.append(p)\n        if 3 < len(png_images):\n            break\n\n    for input_path in png_images:\n        if OUTPUT_BUCKET != "":\n            output_path = Path(f"s3://{OUTPUT_BUCKET}/{input_path.name}")\n            print(f"upload {output_path.name} to {output_path}")\n            output_path.write_bytes(p.read_bytes())\n        else:\n            print(f"skip upload {input_path.name}")\n\n\nif __name__ == "__main__":\n    main()\n```\n\n## Featuers\n| | HttpPath | S3Path| GCSPath |\n| :-------------: | :-------------: | :-------------: | :-------------: |\n| open | ✅ | ✅ | ✅ |\n| read_text | ✅ | ✅ | ✅ |\n| read_byte | ✅ | ✅ | ✅ |\n| write_text | ❌ | ✅ | ✅ |\n| write_byte | ❌ | ✅ | ✅ |\n| iterdir | ❌ | ✅ | ✅ |\n| touch | ❌ | ✅ | ✅ |\n| mkdir | ❌ | ✅ | ✅ |\n| exists | ❌ | ✅ | ✅ |\n\n\n## Roadmap\n\nSee the [open issues](https://github.com/ar90n/paaaaath/issues) for a list of proposed features (and known issues).\n\n## Contributing\n\nContributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.\n\n1. Fork the Project\n2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)\n3. Commit your Changes (`git commit -m \'Add some AmazingFeature\'`)\n4. Push to the Branch (`git push origin feature/AmazingFeature`)\n5. Open a Pull Request\n\n## License\n\nDistributed under the MIT License. See `LICENSE` for more information.\n\n## Contact\n\nMasahiro Wada - [@ar90n](https://twitter.com/ar90n) - argon.argon.argon@gmail.com\n\nProject Link: [https://github.com/ar90n/paaaaath](https://github.com/ar90n/paaaaath)\n\n## Acknowledgements\n\n- [smart-open](https://pypi.org/project/smart-open/)\n- [Python Logo](https://ascii.matthewbarber.io/art/python/)\n\n<!-- MARKDOWN LINKS & IMAGES -->\n<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->\n\n[download-shield]: https://img.shields.io/pypi/dm/paaaaath?style=for-the-badge\n[download-url]: https://pypi.org/project/paaaaath/\n[version-shield]: https://img.shields.io/pypi/v/paaaaath?style=for-the-badge\n[version-url]: https://pypi.org/project/paaaaath/\n[build-shiled]: https://img.shields.io/github/workflow/status/ar90n/paaaaath/CI?style=for-the-badge\n[build-url]: https://github.com/ar90n/paaaaath/actions/workflows/ci.yml\n[contributors-shield]: https://img.shields.io/github/contributors/ar90n/paaaaath.svg?style=for-the-badge\n[contributors-url]: https://github.com/ar90n/paaaaath/graphs/contributors\n[forks-shield]: https://img.shields.io/github/forks/ar90n/paaaaath.svg?style=for-the-badge\n[forks-url]: https://github.com/ar90n/paaaaath/network/members\n[stars-shield]: https://img.shields.io/github/stars/ar90n/paaaaath.svg?style=for-the-badge\n[stars-url]: https://github.com/ar90n/paaaaath/stargazers\n[issues-shield]: https://img.shields.io/github/issues/ar90n/paaaaath.svg?style=for-the-badge\n[issues-url]: https://github.com/ar90n/paaaaath/issues\n[license-shield]: https://img.shields.io/github/license/ar90n/paaaaath.svg?style=for-the-badge\n[license-url]: https://github.com/ar90n/paaaaath/blob/main/LICENSE.txt\n',
    'author': 'Masahiro Wada',
    'author_email': 'argon.argon.argon@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ar90n/paaaaath',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
