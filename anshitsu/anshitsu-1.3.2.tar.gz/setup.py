# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['anshitsu']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.3.1,<10.0.0',
 'colorcorrect>=0.9.1,<0.10.0',
 'fire>=0.4.0,<0.5.0',
 'numpy>=1.21.0,<2.0.0']

entry_points = \
{'console_scripts': ['anshitsu = anshitsu.cli:main']}

setup_kwargs = {
    'name': 'anshitsu',
    'version': '1.3.2',
    'description': 'A tiny digital photographic utility.',
    'long_description': '# Anshitsu\n\n[![Testing](https://github.com/huideyeren/anshitsu/actions/workflows/testing.yml/badge.svg)](https://github.com/huideyeren/anshitsu/actions/workflows/testing.yml)\n\n[![codecov](https://codecov.io/gh/huideyeren/anshitsu/branch/main/graph/badge.svg?token=ZYRX8NBTLQ)](https://codecov.io/gh/huideyeren/anshitsu)\n\nA tiny digital photographic utility.\n\n"Anshitsu" means a darkroom in Japanese.\n\n## Install\n\nRun this command in an environment where Python 3.8 or higher is installed.\n\nWe have tested it on Windows, Mac, and Ubuntu on GitHub Actions, but we have not tested it on Macs with Apple Silicon, so please use it at your own risk on Macs with Apple Silicon.\n\n``` shell\npip install anshitsu\n```\n\n## Usage\n\nIt is as described in the following help.\n\n``` shell\nINFO: Showing help with the command \'anshitsu -- --help\'.\n\nNAME\n    anshitsu - Process Runnner for Command Line Interface\n\nSYNOPSIS\n    anshitsu PATH <flags>\n\nDESCRIPTION\n    This utility converts the colors of images such as photos.\n\n    If you specify a directory path, it will convert\n    the image files in the specified directory.\n    If you specify a file path, it will convert the specified file.\n    If you specify an option, the specified conversion will be performed.\n\n    Tosaka mode is a mode that expresses the preference of\n    Tosaka-senpai, a character in "Kyūkyoku Chōjin R",\n    for "photos taken with Tri-X that look like they were\n    burned onto No. 4 or No. 5 photographic paper".\n    Only use floating-point numbers when using this mode;\n    numbers around 2.4 will make it look right.\n\nPOSITIONAL ARGUMENTS\n    PATH\n        Type: str\n        Directory or File Path\n\nFLAGS\n    --colorautoadjust=COLORAUTOADJUST\n        Type: bool\n        Default: False\n        Use colorautoadjust algorithm. Defaults to False.\n    --colorstretch=COLORSTRETCH\n        Type: bool\n        Default: False\n        Use colorstretch algorithm. Defaults to False.\n    --grayscale=GRAYSCALE\n        Type: bool\n        Default: False\n        Convert to grayscale. Defaults to False.\n    --invert=INVERT\n        Type: bool\n        Default: False\n        Invert color. Defaults to False.\n    --tosaka=TOSAKA\n        Type: Optional[Optional]\n        Default: None\n        Use Tosaka mode. Defaults to None.\n    --outputrgb=OUTPUTRGB\n        Type: bool\n        Default: False\n        Outputs a monochrome image in RGB. Defaults to False.\n    --noise=NOISE\n        Type: Optional[Optional]\n        Default: None\n        Add Gaussian noise. Defaults to None.\n\nNOTES\n    You can also use flags syntax for POSITIONAL ARGUMENTS\n```\n\nIf a directory is specified in the path, an `out` directory will be created in the specified directory, and the converted JPEG and PNG images will be stored in JPEG format.\n\nIf you specify a JPEG or PNG image file as the path, an `out` directory will be created in the directory where the image is stored, and the converted image will be stored in JPEG format.\n\nNote: If you specify\nIf you specify a file of any other format in the path, error handling is not available. An error will probably occur and the program will terminate abnormally.\n\n## Algorithm\n\nThe following algorithms are available in this tool.\n\n### RGBA to RGB Convert\n\nConverts an image that contains Alpha, such as RGBA, to image data that does not contain Alpha.\nTransparent areas will be filled with white.\n\nThis algorithm is performed on any image file.\n\n### invert\n\nInverts the colors of an image using Pillow\'s built-in algorithm.\n\nIn the case of negative film, color conversion that takes into account the film base color is not performed, but we plan to follow up with a feature to be developed in the future.\n\n### colorautoajust\n\nWe will use the "automatic color equalization" algorithm described in the following paper to apply color correction.\n\nThis process is more time consuming than the algorithm used in "colorstretch", but it can reproduce more natural colors.\n\n(References)\n\nA. Rizzi, C. Gatta and D. Marini, "A new algorithm for unsupervised global and local color correction.", Pattern Recognition Letters, vol. 24, no. 11, 2003.\n\n### colorstretch\n\nThe "gray world" and "stretch" algorithms described in the following paper are combined to apply color correction.\n\nThis process is faster than the algorithm used in "colorautoajust".\n\n(References)\n\nD. Nikitenko, M. Wirth and K. Trudel, "Applicability Of White-Balancing Algorithms to Restoring Faded Colour Slides: An Empirical Evaluation.", Journal of Multimedia, vol. 3, no. 5, 2008.\n\n### grayscale\n\nConvert a color image to grayscale using the algorithm described in the following article.\n\n[Python でグレースケール(grayscale)化](https://qiita.com/yoya/items/dba7c40b31f832e9bc2a#pilpillow-%E3%81%A7%E3%82%B0%E3%83%AC%E3%83%BC%E3%82%B9%E3%82%B1%E3%83%BC%E3%83%AB%E5%8C%96-numpy-%E3%81%A7%E4%BD%8E%E8%BC%9D%E5%BA%A6%E5%AF%BE%E5%BF%9C)\n\nNote: This article is written in Japanese.\n\n### Tosaka mode\n\nTosaka mode is a mode that expresses the preference of Tosaka-senpai, a character in "Kyūkyoku Chōjin R", for "photos taken with Tri-X that look like they were burned onto No. 4 or No. 5 photographic paper".\n\nOnly use floating-point numbers when using this mode; numbers around 2.4 will make it look right.\n\nWhen this mode is specified, color images will also be converted to grayscale.\n\n### outputrgb\n\nOutputs a monochrome image in RGB.\n\n### noise\n\nAdd Gaussian noise.\n\nTo add noise, you need to specify floating-point numbers; a value of about 10.0 will be just right.\n\n## Special Thanks\n\nWe are using the following libraries.\n\n[shunsukeaihara/colorcorrect](https://github.com/shunsukeaihara/colorcorrect)\n',
    'author': 'Iosif Takakura',
    'author_email': 'iosif@huideyeren.info',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/huideyeren',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
