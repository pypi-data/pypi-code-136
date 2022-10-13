# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bimato']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.2,<2.0.0',
 'pandas>=1.4.3,<2.0.0',
 'scikit-image>=0.19.3,<0.20.0',
 'scipy>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'bimato',
    'version': '2022.1.2',
    'description': 'Bio Matrix Topology (BiMaTo) is a library containing all the biopolymer matrix topology analyses published by the Biological Physics Group, (BIP), Peter Debye Institute, University Leipzig, Germany.',
    'long_description': 'BiMaTo\n======\n\n|DOI| |GPLv3 license| |PyPI version shields.io| |Documentation Status|\n\n.. |DOI| image:: https://zenodo.org/badge/DOI/10.1038/s41598-019-44764-5.svg\n   :target: https://doi.org/10.1038/s41598-019-44764-5\n\n.. |PyPI version shields.io| image:: https://img.shields.io/pypi/v/bimato.svg\n   :target: https://pypi.python.org/pypi/bimato/\n\n.. |GPLv3 license| image:: https://img.shields.io/badge/License-GPLv3-blue.svg\n   :target: http://perso.crans.org/besson/LICENSE.html\n\n.. |Documentation Status| image:: https://readthedocs.org/projects/bimato/badge/?version=latest\n   :target: http://bimato.readthedocs.io/?badge=latest\n\nBio Matrix Topology (BiMaTo) is a library containing all the biopolymer matrix topology analyses published by the Biological Physics Group, (BIP), Peter Debye Institute, University Leipzig, Germany.\n\nDocumentation can be found `here <https://bimato.readthedocs.io/>`__.\n\nHow to install\n--------------\n\n**bimato** uses Python3.8 and up. Installation is trivial::\n\n    pip install bimato\n\nExemplary analysis workflow\n---------------------------\n\nThis is an exemplary workflow to analyze pore sizes of two different collagen scaffolds. The matrices have been fluorescently stained and 3D images were recorded using an LSM.\n\nUsually, we have for example different collagen scaffolds and want to compare their pore-sizes. For this, we would load several images, calculate their pore-sizes and plot them. Below is an exemplary workflow for this:\n\n- load each image in the LIF file\n- analyze it\n- extract meta-data such as collagen concentration from image name\n- concatenate this data to global DataFrame\n- plot comparison boxplot\n\n..  code-block:: python\n\n    import pandas as pd\n    from readlif.reader import LifFile\n    import seaborn as sns\n    import bimato\n\n    lif_file = LifFile("/path/to/sample.lif")\n\n    df_poresize = list()\n    for lif_image in lif_file.get_iter_image():\n\n        data = bimato.utils.read_lif_image(lif_image)\n        bw = bimato.get_binary(data)\n\n        sampling = {\n            \'x\': 1/lif_image.info["scale"][0],\n            \'y\': 1/lif_image.info["scale"][1],\n            \'z\': 1/lif_image.info["scale"][2]\n        }\n\n        df_tmp = bimato.get_pore_sizes(binary=bw, sampling=sampling)\n\n        df_tmp[\'Concentration [g/l]\'] = lif_image.name\n        df_poresize.append(df_tmp)\n\n    df_poresize = pd.concat(df_poresize)\n\n    g = sns.catplot(\n        data=df_poresize,\n        kind=\'box\',\n        x=\'Concentration [g/l]\',\n        y=\'Diameter [µm],\n    )\n    g.set_ylabels("Pore-size [µm]")\n\nResulting in the following plot:\n\n.. image:: docs/source/poresize_m.jpeg\n  :width: 200\n  :align: center\n  :alt: boxplot of poresize between two differently concengtrated collagen matrices\n\nHow to cite\n-----------\n\nFischer T, Hayn A, Mierke CT (2019) Fast and reliable advanced two-step pore-size analysis of biomimetic 3D extracellular matrix scaffolds. Scientific Reports 9:8352. https://doi.org/10.1038/s41598-019-44764-5\n\n\n.. _article: https://www.nature.com/articles/s41598-019-44764-5',
    'author': 'Tony Fischer (tku137)',
    'author_email': 'tonyfischer@mailbox.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.physgeo.uni-leipzig.de/en/pdi/biological-physics',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
