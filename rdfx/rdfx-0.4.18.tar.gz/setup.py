# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rdfx']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.20.20,<2.0.0',
 'httpx>=0.23.0,<0.24.0',
 'rdflib>=6.0.2,<7.0.0',
 'requests>=2.26.0,<3.0.0']

extras_require = \
{'app': ['streamlit>=1.2.0,<2.0.0', 'python-dotenv>=0.19.2,<0.20.0']}

entry_points = \
{'console_scripts': ['rdfx = rdfx.rdfx_cli:main']}

setup_kwargs = {
    'name': 'rdfx',
    'version': '0.4.18',
    'description': 'Tools for converting, merging, persisting and reading RDF data in different formats.',
    'long_description': '![](https://surroundaustralia.com/themes/custom/surround_australia/surround-logo-dark.svg)\n\n# rdfx\n\nA small Python utility to convert, merge, and read/persist RDF data in different formats, across different "persistence\nsystems".\n\n## How to Use\n\nThe command line utility covers merge and conversion functionality, and simplifies certain aspects of this. The\n\n### Python\n\nRun the `rdfx.py` script with Python having installed the packages required by _requirements.txt_.\n\n### BASH (Linux, Mac etc)\n\nTo utilise the command line util run:\n`python rdfx.py *args`\n\nTo convert a file:\n`python rdfx.py convert myfile.ttl -f nt -o output_dir`\nFor multiple files:\n`python rdfx.py convert myfile1.ttl myfile2.ttl -f nt -o output_dir`\nA directory of files:\n`python rdfx.py convert files_dir -f nt -o output_dir`\nTo merge multiple files:\n`python rdfx.py merge myfile1.ttl myfile2.ttl -f nt -o output_dir`\nTo merge a directory of files:\n`python rdfx.py merge files_dir -f nt -o output_dir`\nTo remove sort and remove unused prefixes in a turtle file:\n`python rdfx.py clean myfile.ttl`\n\nTo simplify usage of the command line utility at present, the following behaviour has been set:\n\nType | Output Filenames\n---|---\nMerge | merged.{format}\nConvert | file1.{format} file2.{format} ...\n\nThat is, when merging, the output filename will be "merged", with the correct file format.\nWhen converting, the output filename will be the same as the input filename, with the correct file format.\nThis behaviour simplifies input to the command line util, allowing multiple files and directories to be input without\nconfusion as to which specified filenames are for input or output, and mappings between input and output, especially\ndirectories or multiple files are converted/merged.\n\nThe python utilities behind the command line tool can be configured to set user specified filenames, for these cases\nuse Python.\n\n### SOP / EDG usage\n\nThe SOP persistence system can be used to read and write to/from EDG master graphs and workflows. The SOP persistence\nsystem can be instantiated with the following optional parameters:\n\n1. location, defaults to "http://localhost:8083"\n2. username, defaults to "Administrator"\n3. password, defaults to ""\n4. timeout, defaults to 60 seconds\n   Example instantiation with defaults:\n\n```\nfrom rdfx.persistence_systems import SOP\nlocal_sop_ps = SOP()\n```\n\nThe following methods are available on instances of the SOP class:\n\n| Method                | Paramters                                                                                                                                            | Returns                           |\n|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|\n| read                  | graph URN<br/> rdf_format                                                                                                                            | list of comments<br/>RDFLib Graph |\n| write                 | RDFLib Graph<br/> graph IRI<br/> list of comments (optional)                                                                                         | The IRI of the created graph      |\n| query                 | query<br/> graph_iri<br/> return_format                                                                                                              | The query results                 |\n| asset_collection_size | asset_iri                                                                                                                                            | Triples count for the given asset |\n| create_datagraph      | datagraph_name (optional) <br/>description (optional)<br/> subjectArea (optional)<br/> default_namespace (optional)<br/>HTTP  headers (optional)     | datagraph IRI                     |\n| create_workflow       | graph_iri<br/> workflow_name (optional)<br/>HTTP  headers (optional)                                                                                 | workflow IRI                      |\n| create_manifest       | manifest_name (optional)<br/> description (optional)<br/> subjectArea (optional)<br/> default_namespace (optional)<br/> HTTP headers (optional)<br/> | the IRI for the manifest          |\n| asset_exists          | graph_name                                                                                                                                           | true/false                        |\n\n### Command line tool documentation\n\nThese usage notes come from running the help command in the tool, e.g. `python rdfx.ph -h`:\n\n```bash\nusage: rdfx.py [-h] [--format {ttl,turtle,json,json-ld,jsonld,owl,xml,rdf,nt,n3}] [-o OUTPUT] [--comments COMMENTS] {convert,merge} data [data ...]\n\npositional arguments:\n  {convert,merge}\n  data                  Path to the RDF file or directory of files for merging or conversion.\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --format {ttl,turtle,json,json-ld,jsonld,owl,xml,rdf,nt,n3}, -f {ttl,turtle,json,json-ld,jsonld,owl,xml,rdf,nt,n3}\n                        The RDFlib token for the RDF format you want to convert the RDF file to.\n  -o OUTPUT, --output OUTPUT\n                        if set, the output location for merged or converted files, defaults to the current working directory\n  --comments COMMENTS   Comments to prepend to the RDF, turtle only.\n```\n\n## License\n\nLGPL - see the [LICENSE file](LICENSE) for details\n\n## Dependencies\n\nThis uses [RDFlib](https://pypi.org/project/rdflib/).\n\n## Contact\n\nOriginal library:\n**Nicholas J. Car**\n*Data Systems Architect*\n[SURROUND Australia Pty Ltd](http://surroundaustralia.com)\n<nicholas.car@surroundaustralia.com>\nGitHub: [nicholascar](https://github.com/nicholascar)\nORCID: <https://orcid.org/0000-0002-8742-7730>\n\nUpdates around persistence systems:\n**David Habgood**\n*Application Architect*\n[SURROUND Australia Pty Ltd](https://surroundaustralia.com)\n<david.habgood@surroundaustrlaia.com>\nGitHub: [nicholascar](https://github.com/recalcitrantsupplant)\nhttps://orcid.org/0000-0002-3322-1868\n',
    'author': 'david-habgood',
    'author_email': 'david.habgood@surroundaustralia.com',
    'maintainer': 'adam-davis',
    'maintainer_email': 'adam.davis@surroundaustralia.com',
    'url': 'https://github.com/surroundaustralia/rdfx',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
