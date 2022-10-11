# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pdfalyzer',
 'pdfalyzer.binary',
 'pdfalyzer.decorators',
 'pdfalyzer.detection',
 'pdfalyzer.detection.constants',
 'pdfalyzer.helpers',
 'pdfalyzer.output',
 'pdfalyzer.util']

package_data = \
{'': ['*'], 'pdfalyzer': ['yara_rules/*']}

install_requires = \
['Deprecated>=1.2.13,<2.0.0',
 'PyPDF2>=2.10,<3.0',
 'anytree>=2.8,<3.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'rich-argparse-plus>=0.3.1,<0.4.0',
 'rich>=12.5.1,<13.0.0',
 'yaralyzer>=0.6.0,<0.7.0']

entry_points = \
{'console_scripts': ['pdfalyze = pdfalyzer:pdfalyze',
                     'pdfalyzer_show_color_theme = '
                     'pdfalyzer.helpers.rich_text_helper:pdfalyzer_show_color_theme']}

setup_kwargs = {
    'name': 'pdfalyzer',
    'version': '1.10.4',
    'description': 'A PDF analysis toolkit. Scan a PDF with relevant YARA rules, visualize its inner tree-like data structure in living color (lots of colors), force decodes of suspicious font binaries, and more.',
    'long_description': '<!-- ![Tests](https://img.shields.io/github/workflow/status/michelcrypt4d4mus/pdfalyzer/tests?label=tests) -->\n![Python Version](https://img.shields.io/pypi/pyversions/pdfalyzer)\n![Release](https://img.shields.io/github/v/release/michelcrypt4d4mus/pdfalyzer?sort=semver)\n![Downloads](https://img.shields.io/pypi/dm/pdfalyzer)\n\n\n# THE PDFALYZER\n\n![Basic Tree](doc/svgs/rendered_images/basic_tree.png)\n\nA PDF analysis tool geared towards visualizing the inner tree-like data structure[^1] of a PDF in [spectacularly large and colorful diagrams](#example-output) as well as scanning the binary streams embedded in the PDF for hidden potentially malicious content.\n\nThe Pdfalyzer makes heavy use of YARA (via [The Yaralyzer](https://github.com/michelcrypt4d4mus/yaralyzer)) for matching/extracting byte patterns. [The Yaralyzer](https://github.com/michelcrypt4d4mus/yaralyzer) actually began its life as The Pdfalyzer\'s matching engine.\n\n**PyPi Users:** If you are reading this document [on PyPi](https://pypi.org/project/pdfalyzer/) be aware that it renders a lot better [over on GitHub](https://github.com/michelcrypt4d4mus/pdfalyzer). Lots of pretty pictures, footnotes that work, etc.\n\n#### Quick Start\n```sh\npipx install pdfalyzer\npdfalyze the_heidiggerian_themes_expressed_in_illmatic.pdf\n```\n\n### What It Do\n1. **Generate in depth visualizations of a PDF\'s tree structure**[^1] that give you a complete picture of all of the PDF\'s internal objects and the links between them. See [the examples below](#example-output) to get an idea.\n1. **Scan for malicious content** both with all the PDF related [YARA](https://github.com/VirusTotal/yara-python) rules I could dig up as well as in-depth scans of the embedded compressed binaries. Some tools don\'t decompress those binaries before scanning.\n1. **Forcibly decode suspicious byte patterns with many different character encodings.** [`chardet`](https://github.com/chardet/chardet) is leveraged to attempt to guess the encoding but no matter what `chardet` thinks the results of forcing the bytes into an encoding will be displayed.\n1. **Be used as a library for your own PDF related code.** All[^2] the inner PDF objects are guaranteed to be available in a searchable tree data structure.\n\nIf you\'re looking for one of these things this may be the tool for you.\n\nAn exception will be raised if there\'s any issue placing a node while parsing or if there are any nodes not reachable from the root of the tree at the end of parsing.\n\n### What It Don\'t Do\nThis tool is mostly about examining a PDF\'s logical structure and assisting with the discovery of malicious content. As such it doesn\'t have much to offer as far as extracting text from PDFs, rendering PDFs[^3], writing new PDFs, or many of the more conventional things one might do with a portable document.\n\n### Did The World Really Need Another PDF Tool?\nThis tool was built to fill a gap in the PDF assessment landscape following [my own recent experience trying to find malicious content in a PDF file](https://twitter.com/Cryptadamist/status/1570167937381826560). Didier Stevens\'s [pdfid.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/pdfid.py) and [pdf-parser.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/pdf-parser.py) are still the best game in town when it comes to PDF analysis tools but they lack in the visualization department and also don\'t give you much to work with as far as giving you a data model you can write your own code around. [Peepdf](https://github.com/jesparza/peepdf) seemed promising but turned out to be in a buggy, out of date, and more or less unfixable state. And neither of them offered much in the way of tooling for embedded binary analysis.\n\nThus I felt the world might be slightly improved if I strung together a couple of more stable/well known/actively maintained open source projects ([AnyTree](https://github.com/c0fec0de/anytree), [PyPDF2](https://github.com/py-pdf/PyPDF2), [Rich](https://github.com/Textualize/rich), and [YARA](https://github.com/VirusTotal/yara-python) via [The Yaralyzer](https://github.com/michelcrypt4d4mus/yaralyzer)) into this tool.\n\n\n\n# Installation\n\n```sh\npipx install pdfalyzer\n```\n\n[pipx](https://pypa.github.io/pipx/) is a tool that basically runs `pip install` for a python package but in such a way that the installed package\'s requirements are isolated from your system\'s python packages. If you don\'t feel like installing `pipx` then `pip install` should work fine as long as there are no conflicts between The Pdfalyzer\'s required packages and those on your system already. (If you aren\'t using other python based command line tools then your odds of a conflict are basically 0%.)\n\nFor info on how to setup a dev environment, see [Contributing](#contributing) section at the end of this file.\n\n### Troubleshooting The Installation\n1. If you used regular `pip3` instead of `pipx` and you only want to use the CLI and don\'t need to `import` the python classes to your own code, you should try to install with `pipx` instead.\n1. If you run into an issue about missing YARA try to install [yara-python](https://pypi.org/project/yara-python/). If that doesn\'t work you may have to install the YARA executable separately.\n1. If you encounter an error building the python `cryptography` package check your `pip` version (`pip --version`). If it\'s less than 22.0, upgrade `pip` with `pip install --upgrade pip`.\n2. On linux if you encounter an error building `wheel` or `cffi` you may need to install some packages like a compiler for the `rust` language or some SSL libraries. `sudo apt-get install build-essential libssl-dev libffi-dev rustc` may help.\n1. While `poetry.lock` is checked into this repo the versions "required" there aren\'t really "required" so feel free to delete or downgrade if you need to.\n\n\n# Usage\nRun `pdfalyze --help` to see usage instructions. As of right now these are the options:\n\n![argparse_help](doc/svgs/rendered_images/pdfalyze_help_prince_theme.png)\n\nNote that The Pdfalyzer output is _extremely_ verbose if you don\'t limit the output sections (See `ANALYSIS SELECTION` in the `--help`). Almost all of the verbosity comes from the `--stream` option. To get everything _except_ the stream option, use these flags\n\n```sh\npdfalyzer lacan_buys_the_dip.pdf -d -t -r -f -y -c\n```\n\nBeyond that there\'s [a few scripts](scripts/) in the repo that may be of interest.\n\n### Setting Command Line Options Permanently With A `.pdfalyzer` File\nIf you find yourself specificying the same options over and over you may be able to automate that with a [dotenv](https://pypi.org/project/python-dotenv/) setup. When you run `pdfalyze` on some PDF the tool will check for a file called `.pdfalyzer` first in the current directory and then in the home directory. If it finds a file in either such place it will load options from it. Documentation on the options that can be configured with these files lives in [`.pdfalyzer.example`](.pdfalyzer.example) which doubles as an example file you can copy into place and edit to your needs. Even if don\'t configure your own `.pdfalyzer` file you may still glean some insight from reading the descriptions of the various variables in [.pdfalyzer.example](.pdfalyzer.example); there\'s a little more exposition there than in the output of `pdfalyze -h`.\n\n### Colors And Themes\nRun `pdfalyzer_show_color_theme` to see the color theme employed.\n\n### As A Code Library\nAt its core The Pdfalyzer is taking PDF internal objects gathered by [PyPDF2](https://github.com/py-pdf/PyPDF2) and wrapping them in [AnyTree](https://github.com/c0fec0de/anytree)\'s `NodeMixin` class.  Given that things like searching the tree or accessing internal properties will be done through those packages\' code it may be quite helpful to review their documentation.\n\nAs far as The Pdfalyzer\'s unique functionality goes, `Pdfalyzer` is the class at the heart of the operation. It holds both the PDF\'s logical tree as well as a couple of other data structures that have been pre-processed to make them easier to work with. Chief among these is the `FontInfo` class which pulls together various properties of a font strewn across 3 or 4 different PDF objects and the `BinaryScanner1` class which lets you dig through the raw bytes looking for suspicious patterns.\n\nHere\'s a short intro to how to access these objects:\n\n```python\nfrom pdfalyzer.pdfalyzer import Pdfalyzer\n\n# Load a PDF and parse its nodes into the tree.\npdfalyzer = Pdfalyzer("/path/to/the/evil.pdf")\nactual_pdf_tree = pdfalyzer.pdf_tree\n\n# Find a PDF object by its ID in the PDF\nnode = pdfalyzer.find_node_by_idnum(44)\npdf_object = node.obj\n\n# Use anytree\'s findall_by_attr to find nodes with a given property\nfrom anytree.search import findall_by_attr\npage_nodes = findall_by_attr(pdfalyzer.pdf_tree, name=\'type\', value=\'/Page\')\n\n# Get the fonts\nfont1 = pdfalyzer.font_infos[0]\n\n# Iterate over backtick quoted strings from a font binary and process them\nfor backtick_quoted_string in font1.binary_scanner.extract_backtick_quoted_bytes():\n    process(backtick_quoted_string)\n\n# Iterate over all stream objects:\nfor node in pdfalyzer.stream_nodes():\n    do_stuff(node.stream_data)\n```\n\n\n### Troubleshooting\nThis tool is by no means complete. It was built to handle a specific use case which encompassed a small fraction of the many and varied types of information that can show up in a PDF. While it has been tested on a decent number of large and very complicated PDFs (500-5,000 page manuals from Adobe itself) I\'m sure there are a whole bunch of edge cases that will trip up the code.\n\nIf that does happen and you run into an issue using this tool on a particular PDF it will most likely be an issue with relationships between objects within the PDF that are not meant to be parent/child in the tree structure made visible by this tool. There\'s not so many of these kinds of object references in any given file but there\'s a whole galaxy of possibilities and they must each be manually configured to prevent the tool from building an invalid tree.  If you run into that kind of problem take a look at these list constants in the code:\n\n* `NON_TREE_REFERENCES`\n* `INDETERMINATE_REFERENCES`\n\nYou might be able to easily fix your problem by adding the Adobe object\'s reference key to the appropriate list.\n\n\n\n\n# Example Output\nThe Pdfalyzer can export visualizations to HTML, ANSI colored text, and SVG images using the file export functionality that comes with [Rich](https://github.com/Textualize/rich). SVGs can be turned into `png` format images with a tool like Inkscape or `cairosvg` (Inkscape works a lot better in our experience).\n\n\n### Basic Tree View\nAs you can see the "mad sus" `/OpenAction` relationship is highlighted bright red, as would be a couple of other suspicious PDF instructions like `/JavaScript` that don\'t exist in the PDF but do exist in other documents.\n\nThe dimmer (as in "harder to see") nodes[^4] marked with `Non Child Reference` give you a way to visualize the relationships between PDF objects that exist outside of the tree structure\'s parent/child relationships.\n\n![Basic Tree](doc/svgs/rendered_images/basic_tree.png)\n\nThat\'s a pretty basic document. [Here\'s the basic tree for a more complicated PDF](doc/svgs/rendered_images/NMAP_Commands_Cheat_Sheet_and_Tutorial.pdf.tree.svg.png).\n\n### Rich Tree View\nThis image shows a more in-depth view of of the PDF tree for the same document shown above. This tree (AKA the "rich" tree) has almost everything. Shows all PDF object properties, all relationships between objects, and sizable previews of any binary data streams embedded or encrypted in the document. Note that in addition to `/OpenAction`, the Adobe Type1 font binary is also red (Google\'s project zero regards any Adobe Type1 font as "mad sus").\n\n![Rich Tree](doc/svgs/rendered_images/rich_table_tree.png)\n\n\n[And here\'s the rich tree for the same more complicated PDF linked to in the Basic Tree section](doc/svgs/rendered_images/NMAP_Commands_Cheat_Sheet_and_Tutorial.pdf.rich_table_tree.png).\n\n\n### Binary Analysis (And Lots Of It)\n#### View the Properties of the Fonts in the PDF\nComes with a preview of the beginning and end of the font\'s raw binary data stream (at least if it\'s that kind of font).\n\n![Font Properties](doc/svgs/rendered_images/font_summary_with_byte_preview.png)\n\n#### Extract Character Mappings from Ancient Adobe Font Formats\nIt\'s actually `PyPDF2` doing the lifting here but we\'re happy to take the credit.\n\n![Font Charmap](doc/svgs/rendered_images/font_character_mapping.png)\n\n#### Search Internal Binary Data for Sus Content No Malware Scanner Will Catch[^5]\nThings like, say, a hidden binary `/F` (PDF instruction meaning "URL") followed by a `JS` (I\'ll let you guess what "JS" stands for) and then a binary `»` character (AKA "the character the PDF specification uses to close a section of the PDF\'s logical structure"). Put all that together and it says that you\'re looking at a secret JavaScript instruction embedded in the encrypted part of a font binary. A secret instruction that causes the PDF renderer to pop out of its frame prematurely as it renders the font.\n\n![Font with JS](doc/svgs/rendered_images/font29.js.1.png)\n\n#### Extract And Decode Binary Patterns\nLike, say, bytes between common regular expression markers that you might want to force a decode of in a lot of different encodings.\n\n![Font Scan Regex](doc/svgs/rendered_images/font_34_frontslash_scan.png)\n\nWhen all is said and done you can see some stats that may help you figure out what the character encoding may or may not be for the bytes matched by those patterns:\n\n![Font Decode Summary](doc/svgs/rendered_images/font29_summary_stats.png)\n\n\n#### Now There\'s Even A Fancy Table To Tell You What The `chardet` Library Would Rank As The Most Likely Encoding For A Chunk Of Binary Data\nBehold the beauty:\n![Basic Tree](doc/svgs/rendered_images/decoding_and_chardet_table_2.png)\n\n\n\n\n# PDF Resources\n\n### 3rd Party Tools\n#### Installing Didier Stevens\'s PDF Analysis Tools\nStevens\'s tools provide comprehensive info about the contents of a PDF, are guaranteed not to trigger the rendering of any malicious content (especially `pdfid.py`), and have been battle tested for well over a decade. It would probably be a good idea to analyze your PDF with his tools before you start working with this one.\n\nIf you\'re lazy and don\'t want to retrieve his tools yourself there\'s [a simple bash script](scripts/install_didier_stevens_pdf_tools.sh) to download them from his github repo and place them in a `tools/` subdirectory off the project root. Just run this:\n\n```sh\nscripts/install_didier_stevens_pdf_tools.sh\n```\n\nIf there is a discrepancy between the output of betweeen his tools and this one you should assume his tool is correct and The Pdfalyzer is wrong until you conclusively prove otherwise.\n\n#### Installing The `t1utils` Font Suite\n`t1utils` is a suite of old but battle tested apps for manipulating old Adobe font formats.  You don\'t need it unless you\'re dealing with an older Type 1 or Type 2 font binary but given that those have been very popular exploit vectors in the past few years it can be extremely helpful. One of the tools in the suite, [`t1disasm`](https://www.lcdf.org/type/t1disasm.1.html), is particularly useful because it decrypts and decompiles Adobe Type 1 font binaries into a more human readable string representation.\n\nThere\'s [a script](scripts/install_t1utils.sh) to help you install the suite if you need it:\n\n```sh\nscripts/install_t1utils.sh\n```\n\n### Documentation\n#### Official Adobe Documentation\n* [Official Adobe PDF 1.7 Specification](https://opensource.adobe.com/dc-acrobat-sdk-docs/standards/pdfstandards/pdf/PDF32000_2008.pdf) - Indispensable map when navigating a PDF forest.\n* [Adobe Type 1 Font Format Specification](https://adobe-type-tools.github.io/font-tech-notes/pdfs/T1_SPEC.pdf) - Official spec for Adobe\'s original font description language and file format. Useful if you have suspicions about malicious fonts. Type1 seems to be the attack vector of choice recently which isn\'t so surprising when you consider that it\'s a 30 year old technology and the code that renders these fonts probably hasn\'t been extensively tested in decades because almost no one uses them anymore outside of people who want to use them as attack vectors.\n* [Adobe CMap and CIDFont Files Specification](https://adobe-type-tools.github.io/font-tech-notes/pdfs/5014.CIDFont_Spec.pdf) - Official spec for the character mappings used by Type1 fonts / basically part of the overall Type1 font specification.\n* [Adobe Type 2 Charstring Format](https://adobe-type-tools.github.io/font-tech-notes/pdfs/5177.Type2.pdf) - Describes the newer Type 2 font operators which are also used in some multiple-master Type 1 fonts.\n\n#### Other Stuff\n* [Didier Stevens\'s free book about malicious PDFs](https://blog.didierstevens.com/2010/09/26/free-malicious-pdf-analysis-e-book/) - The master of the malicious PDFs wrote a whole book about how to analyze them. It\'s an old book but the PDF spec was last changed in 2008 so it\'s still relevant.\n* [Analyzing Malicious PDFs Cheat Sheet](https://zeltser.com/media/docs/analyzing-malicious-document-files.pdf) - Like it says on the tin. If that link fails there\'s a copy [here in the repo](doc/analyzing-malicious-document-files.pdf).\n* [T1Utils Github Repo](https://github.com/kohler/t1utils) - Suite of tools for manipulating Type1 fonts.\n* [`t1disasm` Manual](https://www.lcdf.org/type/t1disasm.1.html) - Probably the most useful part of the T1Utils suite because it can decompile encrypted ancient Adobe Type 1 fonts into something human readable.\n\n\n\n# Contributing\nOne easy way of contributing is to run [the script to test against all the PDFs in `~/Documents`](scripts/test_against_all_pdfs_in_Documents_folder.sh) and reporting any issues.\n\nBeyond that see [CONTRIBUTING.md](CONTRIBUTING.md).\n\n# TODO\n* highlight decodes done at `chardet`s behest\n* Highlight decodes with a lot of Javascript keywords\n* deal with repetitive matches\n* https://github.com/1Project/Scanr/blob/master/emulator/emulator.py\n# https://github.com/mandiant/flare-floss\n\n\n\n[^1]: The official Adobe PDF specification calls this tree the PDF\'s "logical structure", which is a good example of nomenclature that does not help those who see it understand anything about what is being described. I can forgive them given that they named this thing back in the 80s, though it\'s a good example of why picking good names for things at the beginning is so important.\n\n[^2]: All internal PDF objects are guaranteed to exist in the tree except in these situations when warnings will be printed:\n  `/ObjStm` (object stream) is a collection of objects in a single stream that will be unrolled into its component objects.\n  `/XRef` Cross-reference stream objects which hold the same references as the `/Trailer` are hacked in as symlinks of the `/Trailer`\n\n[^3]: Given the nature of the PDFs this tool is meant to be scan anything resembling "rendering" the document is pointedly NOT offered.\n\n[^4]: Technically they are `SymlinkNodes`, a really nice feature of [AnyTree](https://github.com/c0fec0de/anytree).\n\n[^5]: At least they weren\'t catching it as of September 2022.\n\n',
    'author': 'Michel de Cryptadamus',
    'author_email': 'michel@cryptadamus.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/michelcrypt4d4mus/pdfalyzer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
