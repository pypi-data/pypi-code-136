#!/usr/bin/env python
#   -*- coding: utf-8 -*-

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'pypbars',
        version = '0.1.12',
        description = 'Provides a convenient way to display progress bars for concurrent asyncio or multiprocessing Pool processes.',
        long_description = '# pypbars\n[![build](https://github.com/soda480/pypbars/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/soda480/pypbars/actions/workflows/main.yml)\n[![Code Grade](https://api.codiga.io/project/34681/status/svg)](https://app.codiga.io/hub/project/34681/pypbars)\n[![coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://pybuilder.io/)\n[![vulnerabilities](https://img.shields.io/badge/vulnerabilities-None-brightgreen)](https://pypi.org/project/bandit/)\n[![PyPI version](https://badge.fury.io/py/pypbars.svg)](https://badge.fury.io/py/pypbars)\n[![python](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-teal)](https://www.python.org/downloads/)\n\nThe `pypbars` module provides a convenient way to display progress bars for concurrent [asyncio](https://docs.python.org/3/library/asyncio.html) or [multiprocessing Pool](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool) processes. The `pypbars` class is a subclass of [list2term](https://pypi.org/project/list2term/) that displays a list to the terminal, and uses [progress1bar](https://pypi.org/project/progress1bar/) to render the progress bar.\n\n### Installation\n```bash\npip install pypbars\n```\n\n#### [example1 - ProgressBars with asyncio](https://github.com/soda480/pypbars/blob/main/examples/example1.py)\n\nCreate `ProgressBars` using a lookup list containing unique values, these identifiers will be used to get the index of the appropriate `ProgressBar` to be updated. The convention is for the function to include `logger.write` calls containing the identifier and a message for when and how the respective progress bar should be updated. In this example the default `regex` dict is used but the caller can specify their own, so long as it contains regular expressions for how to detect when `total`, `count` and optional `alias` are set.\n\n<details><summary>Code</summary>\n\n```Python\nimport asyncio\nimport random\nfrom faker import Faker\nfrom pypbars import ProgressBars\n\nasync def do_work(worker, logger=None):\n    logger.write(f\'{worker}->worker is {worker}\')\n    total = random.randint(10, 65)\n    logger.write(f\'{worker}->processing total of {total} items\')\n    for count in range(total):\n        # mimic an IO-bound process\n        await asyncio.sleep(.1)\n        logger.write(f\'{worker}->processed {count}\')\n    return total\n\nasync def run(workers):\n    with ProgressBars(lookup=workers, show_prefix=False, show_fraction=False) as logger:\n        doers = (do_work(worker, logger=logger) for worker in workers)\n        return await asyncio.gather(*doers)\n\ndef main():\n    workers = [Faker().user_name() for _ in range(10)]\n    print(f\'Total of {len(workers)} workers working concurrently\')\n    results = asyncio.run(run(workers))\n    print(f\'The {len(workers)} workers processed a total of {sum(results)} items\')\n\nif __name__ == \'__main__\':\n    main()\n```\n\n</details>\n\n![example1](https://raw.githubusercontent.com/soda480/pypbars/main/docs/images/example1.gif)\n\n#### [example2 - ProgressBars with multiprocessing Pool](https://github.com/soda480/pypbars/blob/main/examples/example2.py)\n\nThis example demonstrates how `pypbars` can be used to display progress bars from processes executing in a [multiprocessing Pool](https://docs.python.org/3/library/multiprocessing.html#using-a-pool-of-workers). The `list2term.multiprocessing` module contains a `pool_map` method that fully abstracts the required multiprocessing constructs, you simply pass it the function to execute, an iterable containing the arguments to pass each process, and an instance of `ProgressBars`. The method will execute the functions asynchronously, update the progress bars accordingly and return a multiprocessing.pool.AsyncResult object. Each progress bar in the terminal represents a background worker process.\n\nIf you do not wish to use the abstraction, the `list2term.multiprocessing` module contains helper classes that facilitate communication between the worker processes and the main process; the `QueueManager` provide a way to create a `LinesQueue` queue which can be shared between different processes. Refer to [example3](https://github.com/soda480/pypbars/blob/main/examples/example3.py) for how the helper methods can be used. \n\n**Note** the function being executed must accept a `LinesQueue` object that is used to write messages via its `write` method, this is the mechanism for how messages are sent from the worker processes to the main process, it is the main process that is displaying the messages to the terminal. The messages must be written using the format `{identifier}->{message}`, where {identifier} is a string that uniquely identifies a process, defined via the lookup argument to `ProgressBars`.\n\n<details><summary>Code</summary>\n\n```Python\nimport time\nfrom pypbars import ProgressBars\nfrom list2term.multiprocessing import pool_map\nfrom list2term.multiprocessing import CONCURRENCY\n\ndef is_prime(num):\n    if num == 1:\n        return False\n    for i in range(2, num):\n        if (num % i) == 0:\n            return False\n    else:\n        return True\n\ndef count_primes(start, stop, logger):\n    workerid = f\'{start}:{stop}\'\n    logger.write(f\'{workerid}->worker is {workerid}\')\n    logger.write(f\'{workerid}->processing total of {stop - start} items\')\n    primes = 0\n    for number in range(start, stop):\n        if is_prime(number):\n            primes += 1\n        logger.write(f\'{workerid}->processed {number}\')\n    logger.write(f\'{workerid}->{workerid} processing complete\')\n    return primes\n\ndef main(number):\n    step = int(number / CONCURRENCY)\n    iterable = [(index, index + step) for index in range(0, number, step)]\n    lookup = [\':\'.join(map(str, item)) for item in iterable]\n    progress_bars = ProgressBars(lookup=lookup, show_prefix=False, show_fraction=False, use_color=True)\n    # print to screen with progress bars context\n    results = pool_map(count_primes, iterable, context=progress_bars)\n    # print to screen without progress bars context\n    # results = pool_map(count_primes, iterable)\n    # do not print to screen\n    # results = pool_map(count_primes, iterable, print_status=False)\n    return sum(results.get())\n\nif __name__ == \'__main__\':\n    start = time.perf_counter()\n    number = 50_000\n    result = main(number)\n    stop = time.perf_counter()\n    print(f"Finished in {round(stop - start, 2)} seconds\\nTotal number of primes between 0-{number}: {result}")\n```\n\n</details>\n\n![example2](https://raw.githubusercontent.com/soda480/pypbars/main/docs/images/example2.gif)\n\n### Development\n\nClone the repository and ensure the latest version of Docker is installed on your development server.\n\nBuild the Docker image:\n```sh\ndocker image build \\\n-t \\\npypbars:latest .\n```\n\nRun the Docker container:\n```sh\ndocker container run \\\n--rm \\\n-it \\\n-v $PWD:/code \\\npypbars:latest \\\nbash\n```\n\nExecute the build:\n```sh\npyb -X\n```\n',
        long_description_content_type = 'text/markdown',
        classifiers = [
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10'
        ],
        keywords = '',

        author = 'Emilio Reyes',
        author_email = 'soda480@gmail.com',
        maintainer = '',
        maintainer_email = '',

        license = 'Apache License, Version 2.0',

        url = 'https://github.com/soda480/pypbars',
        project_urls = {},

        scripts = [],
        packages = ['pypbars'],
        namespace_packages = [],
        py_modules = [],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = [
            'list2term~=0.1.4',
            'progress1bar~=0.2.7'
        ],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        python_requires = '',
        obsoletes = [],
    )
