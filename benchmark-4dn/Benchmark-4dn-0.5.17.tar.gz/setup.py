# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['Benchmark']

package_data = \
{'': ['*'], 'Benchmark': ['aws/*']}

setup_kwargs = {
    'name': 'benchmark-4dn',
    'version': '0.5.17',
    'description': 'Benchmark functions that returns total space, mem, cpu given input size and parameters for the CWL workflows',
    'long_description': "The repo contains a benchmarking script for some of the CWL workflows used by 4DN-DCIC (https://github.com/4dn-dcic/pipelines-cwl), that returns total space, mem and CPUs required per given input size and a recommended AWS EC2 instance type.\n\n[![Build Status](https://travis-ci.org/SooLee/Benchmark.svg?branch=master)](https://travis-ci.org/SooLee/Benchmark)\n\n### Example usage of benchmarking script\n* importing the module\n```python\nfrom Benchmark import run as B\n```\n\n* md5\n```python\napp_name = 'md5'\ninput_json = {'input_size_in_bytes': {'input_file': 20000}}\nB.benchmark(app_name, input_json)\n```\n```\n{'aws': {'recommended_instance_type': 't2.xlarge', 'EBS_optimized': False, 'cost_in_usd': 0.188, 'EBS_optimization_surcharge': None, 'mem_in_gb': 16.0, 'cpu': 4}, 'total_size_in_GB': 14.855186462402344, 'total_mem_in_MB': 13142.84375, 'min_CPU': 4}\n```\n\n* fastqc-0-11-4-1\n```python\napp_name = 'fastqc-0-11-4-1'\ninput_json = {'input_size_in_bytes': {'input_fastq':20000},\n              'parameters': {'threads': 2}}\nB.benchmark(app_name, input_json)\n```\n```\n{'recommended_instance_type': 't2.nano', 'EBS_optimized': False, 'cost_in_usd': 0.006, 'EBS_optimization_surcharge': None, 'mem_in_gb': 0.5, 'cpu': 1}\n```\n\n* bwa-mem\n```python\napp_name = 'bwa-mem'\ninput_json = {'input_size_in_bytes': {'fastq1':93520000,\n                                      'fastq2':97604000,\n                                      'bwa_index':3364568000},\n              'parameters': {'nThreads': 4}}\nB.benchmark(app_name, input_json)\n```\n```\n{'aws': {'cost_in_usd': 0.188, 'EBS_optimization_surcharge': None, 'EBS_optimized': False, 'cpu': 4, 'mem_in_gb': 16.0, 'recommended_instance_type': 't2.xlarge'}, 'total_mem_in_MB': 12834.808349609375, 'total_size_in_GB': 15.502477258443832, 'min_CPU': 4}\n```\n\nTo use Benchmark in from other places, install it as below.\n```\npip install Benchmark-4dn\n```\nor\n```\npip install git+git://github.com/SooLee/Benchmark.git\n```\n\n\n---\n\nNote: From `0.5.3` we have a new function that takes in cpu and memory and returns a sorted list of instance dictionaries.\n```\nget_instance_types(cpu=1, mem_in_gb=0.5, instances=instance_list(), top=10, rank='cost_in_usd')\n```\n\nKeys in each instance dictionary:\n```\n'cost_in_usd', 'mem_in_gb', 'cpu', 'instance_type', 'EBS_optimized', 'EBS_optimization_surcharge'\n```\n",
    'author': 'Soo Lee',
    'author_email': 'duplexa@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/SooLee/Benchmark/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
