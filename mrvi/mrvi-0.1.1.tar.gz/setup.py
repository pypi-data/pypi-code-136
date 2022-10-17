# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mrvi']

package_data = \
{'': ['*']}

install_requires = \
['anndata>=0.7.5', 'scvi-tools>=0.17.0']

extras_require = \
{':(python_version < "3.8") and (extra == "docs")': ['typing_extensions'],
 ':python_version < "3.8"': ['importlib-metadata>=1.0,<2.0'],
 'dev': ['black>=20.8b1',
         'codecov>=2.0.8',
         'flake8>=3.7.7',
         'isort>=5.7',
         'jupyter>=1.0',
         'loompy>=3.0.6',
         'nbconvert>=5.4.0',
         'nbformat>=4.4.0',
         'pre-commit>=2.7.1',
         'pytest>=4.4',
         'scanpy>=1.6'],
 'docs': ['ipython>=7.1.1',
          'nbsphinx',
          'nbsphinx-link',
          'pydata-sphinx-theme>=0.4.0',
          'scanpydoc>=0.5',
          'sphinx>=4.1,<4.4',
          'sphinx-autodoc-typehints',
          'sphinx-rtd-theme']}

setup_kwargs = {
    'name': 'mrvi',
    'version': '0.1.1',
    'description': 'Multi-resolution analysis of single-cell data.',
    'long_description': '# Multi-resolution Variational Inference\n\nMulti-resolution Variational Inference (MrVI) is a package for analysis of sample-level heterogeneity in multi-site, multi-sample single-cell omics data. Built with [scvi-tools](https://scvi-tools.org).\n\n---\n\nTo install, run:\n\n```\npip install mrvi\n```\n\n`mrvi.MrVI` follows the same API used in scvi-tools.\n\n```python\nimport mrvi\nimport anndata\n\nadata = anndata.read_h5ad("path/to/adata.h5ad")\n#\xa0Sample (e.g. donors, perturbations, etc.) should go in sample_key\n# Sites, plates, and other factors should go in categorical_nuisance_keys\nmrvi.MrVI.setup_anndata(adata, sample_key="donor", categorical_nuisance_keys=["site"])\nmrvi_model = mrvi.MrVI(adata)\nmrvi_model.train()\n# Get z representation\nadata.obsm["X_mrvi_z"] = mrvi_model.get_latent_representation(give_z=True)\n# Get u representation\nadata.obsm["X_mrvi_u"] = mrvi_model.get_latent_representation(give_z=False)\n# Cells by n_sample by n_latent\ncell_sample_representations = mrvi_model.get_local_sample_representation()\n# Cells by n_sample by n_sample\ncell_sample_sample_distances = mrvi_model.get_local_sample_representation(return_distances=True)\n```\n\n## Citation\n\n```\n@article {Boyeau2022.10.04.510898,\n\tauthor = {Boyeau, Pierre and Hong, Justin and Gayoso, Adam and Jordan, Michael and Azizi, Elham and Yosef, Nir},\n\ttitle = {Deep generative modeling for quantifying sample-level heterogeneity in single-cell omics},\n\telocation-id = {2022.10.04.510898},\n\tyear = {2022},\n\tdoi = {10.1101/2022.10.04.510898},\n\tpublisher = {Cold Spring Harbor Laboratory},\n\tabstract = {Contemporary single-cell omics technologies have enabled complex experimental designs incorporating hundreds of samples accompanied by detailed information on sample-level conditions. Current approaches for analyzing condition-level heterogeneity in these experiments often rely on a simplification of the data such as an aggregation at the cell-type or cell-state-neighborhood level. Here we present MrVI, a deep generative model that provides sample-sample comparisons at a single-cell resolution, permitting the discovery of subtle sample-specific effects across cell populations. Additionally, the output of MrVI can be used to quantify the association between sample-level metadata and cell state variation. We benchmarked MrVI against conventional meta-analysis procedures on two synthetic datasets and one real dataset with a well-controlled experimental structure. This work introduces a novel approach to understanding sample-level heterogeneity while leveraging the full resolution of single-cell sequencing data.Competing Interest StatementN.Y. is an advisor and/or has equity in Cellarity, Celsius Therapeutics, and Rheos Medicine.},\n\tURL = {https://www.biorxiv.org/content/early/2022/10/06/2022.10.04.510898},\n\teprint = {https://www.biorxiv.org/content/early/2022/10/06/2022.10.04.510898.full.pdf},\n\tjournal = {bioRxiv}\n}\n```\n',
    'author': 'Pierre Boyeau',
    'author_email': 'pierreboyeau@berkeley.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/YosefLab/mrvi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.2,<4.0',
}


setup(**setup_kwargs)
