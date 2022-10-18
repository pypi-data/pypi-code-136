# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['onto_vae']

package_data = \
{'': ['*'], 'onto_vae': ['data/*']}

install_requires = \
['colorcet>=3.0.0',
 'goatools>=1.0.15',
 'pandas>=1.1.0',
 'seaborn>=0.11.0',
 'torch>=1.10.0',
 'tqdm>=4.60.0']

setup_kwargs = {
    'name': 'onto-vae',
    'version': '0.1.0',
    'description': 'Package to preprocess ontologies, train OntoVAE models and obtain pathway activities.',
    'long_description': "# OntoVAE\nOntoVAE is a package that can be used to integrate biological ontologies into latent space and decoder of Variational Autoencoder models. \nThis allows direct retrieval of pathway activities from the model.\nOntoVAE can also be used to simulate genetic or drug induced perturbations, as demonstrated in our manuscript \n'Biologically informed variational autoencoders allow predictive modeling of genetic and drug induced perturbations'.\n\n## Installation\n\nIn the future, installation via pip will be supported. For now, you can install the package through github as follows:\n\n```\ngit clone https://github.com/hdsu-bioquant/onto-vae.git\ncd onto-vae\n```\nIt is best to first create a new environment, e.g. with conda, and then install the package inside.\n\n```\nconda create -n ontovae python=3.7\nconda activate ontovae\npip install -r requirements.txt\n```\n\nFor on example on how to use our package, please see the Vignette! If you want to run the Vignette as Jupyter notebook, inside your conda environment, also install Jupyter and then open the jupyter notebook:\n\n```\nconda install jupyter\njupyter notebook\n```\n",
    'author': 'daria-dc',
    'author_email': 'daria.doncevic@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/hdsu-bioquant/onto-vae',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
