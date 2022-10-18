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
        name = 'list2term',
        version = '0.1.5',
        description = 'Provides a convenient way to mirror a list to the terminal and helper methods to display messages from concurrent asyncio or multiprocessing Pool processes.',
        long_description = '# list2term\n[![build](https://github.com/soda480/list2term/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/soda480/list2term/actions/workflows/main.yml)\n[![Code Grade](https://api.codiga.io/project/34678/status/svg)](https://app.codiga.io/hub/project/34678/list2term)\n[![coverage](https://img.shields.io/badge/coverage-93%25-brightgreen)](https://pybuilder.io/)\n[![vulnerabilities](https://img.shields.io/badge/vulnerabilities-None-brightgreen)](https://pypi.org/project/bandit/)\n[![PyPI version](https://badge.fury.io/py/list2term.svg)](https://badge.fury.io/py/list2term)\n[![python](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-teal)](https://www.python.org/downloads/)\n\nThe `list2term` module provides a convenient way to mirror a list to the terminal and helper methods to display messages from concurrent [asyncio](https://docs.python.org/3/library/asyncio.html) or [multiprocessing Pool](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool) processes. The `list2term.Lines` class is a subclass of [collections.UserList](https://docs.python.org/3/library/collections.html#collections.UserList) and is tty aware thus it is safe to use in non-tty environments. This class takes a list instance as an argument and when instantiated is accessible via the data attribute. The list can be any iterable, but its elements need to be printable; they should implement __str__ function. The intent of this class is to display relatively small lists to the terminal and dynamically update the terminal when list elements are upated, added or removed. Thus it is able to mirror a List of objects to the terminal.\n\n### Installation\n```bash\npip install list2term\n```\n\n#### [example1 - display list of static size](https://github.com/soda480/list2term/blob/main/examples/example1.py)\n\nCreate an empty list then add sentences to the list at random indexes. As sentences are updated within the list the respective line in the terminal is updated.\n\n<details><summary>Code</summary>\n\n```Python\nimport time\nimport random\nfrom faker import Faker\nfrom list2term import Lines\n\ndef main():\n    print(\'Generating random sentences...\')\n    docgen = Faker()\n    with Lines(size=15, show_x_axis=True, max_chars=100) as lines:\n        for _ in range(200):\n            index = random.randint(0, len(lines) - 1)\n            lines[index] = docgen.sentence()\n            time.sleep(.05)\n\nif __name__ == \'__main__\':\n    main()\n```\n\n</details>\n\n![example1](https://raw.githubusercontent.com/soda480/list2term/main/docs/images/example1.gif)\n\n#### [example2 - display list of dynamic size](https://github.com/soda480/list2term/blob/main/examples/example2.py)\n\nCreate an empty list then add sentences to the list at random indexes. As sentences are updated within the list the respective line in the terminal is updated. Also show how the terminal behaves when new items are added to the list and when items are removed from the list.\n\n<details><summary>Code</summary>\n\n```Python\nimport time\nimport random\nfrom faker import Faker\nfrom list2term import Lines\n\ndef main():\n    print(\'Generating random sentences...\')\n    docgen = Faker()\n    with Lines(data=[\'\'] * 10, max_chars=100) as lines:\n        for _ in range(100):\n            index = random.randint(0, len(lines) - 1)\n            lines[index] = docgen.sentence()\n        for _ in range(100):\n            update = [\'update\'] * 18\n            append = [\'append\'] * 18\n            pop = [\'pop\'] * 14\n            clear = [\'clear\']\n            choice = random.choice(append + pop + clear + update)\n            if choice == \'pop\':\n                if len(lines) > 0:\n                    index = random.randint(0, len(lines) - 1)\n                    lines.pop(index)\n            elif choice == \'append\':\n                lines.append(docgen.sentence())\n            elif choice == \'update\':\n                if len(lines) > 0:\n                    index = random.randint(0, len(lines) - 1)\n                    lines[index] = docgen.sentence()\n            else:\n                if len(lines) > 0:\n                    lines.pop()\n                if len(lines) > 0:\n                    lines.pop()\n            time.sleep(.1)\n\nif __name__ == \'__main__\':\n    main()\n```\n\n</details>\n\n![example2](https://raw.githubusercontent.com/soda480/list2term/main/docs/images/example2.gif)\n\n#### [example3 - display messages from asyncio processes](https://github.com/soda480/pypbars/blob/main/examples/example3.py)\n\nThis example demonstrates how `list2term` can be used to display messages from asyncio processes. Each line in the terminal represents a asnycio process.\n\n<details><summary>Code</summary>\n\n```Python\nimport asyncio\nimport random\nimport uuid\nfrom faker import Faker\nfrom list2term import Lines\n\nasync def do_work(worker, logger=None):\n    logger.write(f\'{worker}->worker is {worker}\')\n    total = random.randint(10, 65)\n    logger.write(f\'{worker}->{worker}processing total of {total} items\')\n    for _ in range(total):\n        # mimic an IO-bound process\n        await asyncio.sleep(random.choice([.05, .1, .15]))\n        logger.write(f\'{worker}->processed {Faker().name()}\')\n    return total\n\nasync def run(workers):\n    with Lines(lookup=workers, use_color=True) as logger:\n        doers = (do_work(worker, logger=logger) for worker in workers)\n        return await asyncio.gather(*doers)\n\ndef main():\n    workers = [Faker().user_name() for _ in range(12)]\n    print(f\'Total of {len(workers)} workers working concurrently\')\n    results = asyncio.run(run(workers))\n    print(f\'The {len(workers)} workers processed a total of {sum(results)} items\')\n\nif __name__ == \'__main__\':\n    main()\n```\n\n</details>\n\n![example3](https://raw.githubusercontent.com/soda480/list2term/main/docs/images/example3.gif)\n\n\n#### [example4 - display messages from multiprocessing Pool processes](https://github.com/soda480/list2term/blob/main/examples/example4.py)\n\nThis example demonstrates how `list2term` can be used to display messages from processes executing in a [multiprocessing Pool](https://docs.python.org/3/library/multiprocessing.html#using-a-pool-of-workers). The `list2term.multiprocessing` module contains a `pool_map` method that fully abstracts the required multiprocessing constructs, you simply pass it the function to execute, an iterable of arguments to pass each process, and an optional instance of `Lines`. The method will execute the functions asynchronously, update the terminal lines accordingly and return a multiprocessing.pool.AsyncResult object. Each line in the terminal represents a background worker process.\n\nIf you do not wish to use the abstraction, the `list2term.multiprocessing` module contains helper classes that facilitates communication between the worker processes and the main process; the `QueueManager` provide a way to create a `LinesQueue` queue which can be shared between different processes. Refer to [example4b](https://github.com/soda480/list2term/blob/main/examples/example4b.py) for how the helper methods can be used.\n\n**Note** the function being executed must accept a `LinesQueue` object that is used to write messages via its `write` method, this is the mechanism for how messages are sent from the worker processes to the main process, it is the main process that is displaying the messages to the terminal. The messages must be written using the format `{identifier}->{message}`, where {identifier} is a string that uniquely identifies a process, defined via the lookup argument to `Lines`.\n\n<details><summary>Code</summary>\n\n```Python\nimport time\nfrom list2term import Lines\nfrom list2term.multiprocessing import pool_map\nfrom list2term.multiprocessing import CONCURRENCY\n\n\ndef is_prime(num):\n    if num == 1:\n        return False\n    for i in range(2, num):\n        if (num % i) == 0:\n            return False\n    else:\n        return True\n\ndef count_primes(start, stop, logger):\n    workerid = f\'{start}:{stop}\'\n    logger.write(f\'{workerid}->processing total of {stop - start} items\')\n    primes = 0\n    for number in range(start, stop):\n        if is_prime(number):\n            primes += 1\n            logger.write(f\'{workerid}->{workerid} {number} is prime\')\n    logger.write(f\'{workerid}->{workerid} processing complete\')\n    return primes\n\ndef main(number):\n    step = int(number / CONCURRENCY)\n    print(f"Distributing {int(number / step)} ranges across {CONCURRENCY} workers running concurrently")\n    iterable = [(index, index + step) for index in range(0, number, step)]\n    lookup = [\':\'.join(map(str, item)) for item in iterable]\n    lines = Lines(lookup=lookup, use_color=True, show_index=True, show_x_axis=False)\n    # print to screen with lines context\n    results = pool_map(count_primes, iterable, context=lines, processes=None)\n    # print to screen without lines context\n    # results = pool_map(count_primes, iterable)\n    # do not print to screen\n    # results = pool_map(count_primes, iterable, print_status=False)\n    return sum(results.get())\n\nif __name__ == \'__main__\':\n    start = time.perf_counter()\n    number = 100_000\n    result = main(number)\n    stop = time.perf_counter()\n    print(f"Finished in {round(stop - start, 2)} seconds\\nTotal number of primes between 0-{number}: {result}")\n```\n\n</details>\n\n![example4](https://raw.githubusercontent.com/soda480/list2term/main/docs/images/example4.gif)\n\n\n#### Other examples\n\nA Conway [Game-Of-Life](https://github.com/soda480/game-of-life) implementation that uses `list2term` to display game to the terminal.\n\n\n### Development\n\nClone the repository and ensure the latest version of Docker is installed on your development server.\n\nBuild the Docker image:\n```sh\ndocker image build \\\n-t \\\nlist2term:latest .\n```\n\nRun the Docker container:\n```sh\ndocker container run \\\n--rm \\\n-it \\\n-v $PWD:/code \\\nlist2term:latest \\\nbash\n```\n\nExecute the build:\n```sh\npyb -X\n```\n',
        long_description_content_type = 'text/markdown',
        classifiers = [
            'License :: OSI Approved :: Apache Software License',
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

        url = 'https://github.com/soda480/list2term',
        project_urls = {},

        scripts = [],
        packages = ['list2term'],
        namespace_packages = [],
        py_modules = [],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = [
            'colorama',
            'cursor'
        ],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        python_requires = '',
        obsoletes = [],
    )
