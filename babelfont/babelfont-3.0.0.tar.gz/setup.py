# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['babelfont', 'babelfont.convertors', 'babelfont.fontFilters']

package_data = \
{'': ['*']}

install_requires = \
['cu2qu>=1.6.7,<2.0.0',
 'fontfeatures>=1.0.6,<2.0.0',
 'fonttools>=4.21.1',
 'glyphsLib>=5.3.2',
 'openstep-plist>=0.2.2',
 'orjson>=3.5.1,<4.0.0',
 'ufoLib2>=0.11.1']

entry_points = \
{'console_scripts': ['babelfont = babelfont.__main__:main']}

setup_kwargs = {
    'name': 'babelfont',
    'version': '3.0.0',
    'description': 'Load, examine and save fonts in a variety of formats',
    'long_description': '# Babelfont: Load, examine and save fonts in a variety of formats\n\n*This describes Babelfont >3.0, which is a complete rewrite from the previous version.*\n\nBabelfont is a utility for loading fonts and examining fonts in a variety\nof formats. It can also be used to *write* fonts in some of these formats,\nmaking it possible to convert between font formats.\n\nHere are the formats which are currently supported:\n\n| Format         | Read    | Write |\n|----------------|---------|-------|\n| Glyphs 2       | *       | *     |\n| Glyphs 3       | *       | *     |\n| .glyphspackage | *       |       |\n| UFO            | *       |       |\n| Designspace    | *       |       |\n| Fontlab VFJ    | partial |       |\n| TTF            | partial | *     |\n| OTF            | partial |       |\n| Babelfont      | *       | *     |\n\nBabelfont converts all of the above font formats into a intermediary\nset of objects, whose object hierarchy can be seen [here](https://simoncozens.github.io/babelfont). The allows\nthe developer to examine any font (single master or variable), without\nneeding to worry about the details of each font format.\n\nFor example:\n\n```python\nfrom babelfont import load\n\nfont = load("Myfont.glyphs") # Or .designspace, or whatever\ndefault_a = font.default_master.get_glyph_layer("A")\ntop_anchor = default_a.anchors_dict["top"].x\nprint("Top anchor = (%i,%i)" % (top_anchor.x, top_anchor.y))\nprint("LSB, RSB = (%i,%i)" % (default_a.lsb, default_a.rsb))\nfont.save("Myfont.ttf")\n```\n',
    'author': 'Simon Cozens',
    'author_email': 'simon@simon-cozens.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
