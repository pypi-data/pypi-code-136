# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ladok3']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0',
 'argcomplete>=2.0.0,<3.0.0',
 'cachetools>=5.2.0,<6.0.0',
 'cryptography>=37.0.3,<38.0.0',
 'keyring>=23.6.0,<24.0.0',
 'requests>=2.28.0,<3.0.0',
 'urllib3>=1.26.9,<2.0.0']

entry_points = \
{'console_scripts': ['ladok = ladok3.cli:main']}

setup_kwargs = {
    'name': 'ladok3',
    'version': '1.20',
    'description': 'Python wrapper and CLI for the LADOK3 REST API.',
    'long_description': '# ladok3: Python wrapper for LADOK3 API\n\nThis package provides a wrapper for the LADOK3 API used by \n[start.ladok.se][ladok]. This makes it easy to automate reporting grades, \ncompute statistics etc.\n\n## Installation\n\nTo install, run:\n```bash\npip install ladok3\nsudo cp $(find / -name ladok.bash) /etc/bash_completion.d\nladok login\n```\nIf you run the second line above, you\'ll get tab completion for the `ladok` \ncommand when you use the `bash` shell.\n\nThe third command above is to log in, you only do this once.\n\nAn alternative to installing the package is to run the [Docker image][docker].\n```bash\ndocker run -it dbosk/ladok3 /bin/bash\n```\nOr simply adapt your own image.\n\n## Usage\n\nThere are two ways to use the package: as a Python package or through the \ncommand-line tool `ladok`.\n\n### On the command line\n\nLet\'s assume that we have a student with personnummer 123456-1234.\nLet\'s also assume that this student has taken a course with course code AB1234 \nand finished the module LAB1 on date 2021-03-15.\nThen we can report this result like this:\n```bash\nladok report 123456-1234 AB1234 LAB1 -d 2021-03-15 -f\n```\n\nIf we use Canvas for all results, we can even report all results for a \ncourse.\n```bash\npip install canvaslms\ncanvaslms login\ncanvaslms results -c AB1234 -A LAB1 | ladok report -v\n```\nThe `canvaslms results` command will export the results in CSV format, this \nwill be piped to `ladok report` that can read it and report it in bulk.\n\n### As a Python package\n\nTo use the package, it\'s just to import the package as usual.\n```python\nimport ladok3\n\nls = ladok3.LadokSessionKTH("user", "password")\n\nstudent = ls.get_student("123456-1234")\n\ncourse_participation = student.courses(code="AB1234")[0]\nfor result in course_participation.results():\n  print(f"{course_participation.code} {result.component}: "\n    f"{result.grade} ({result.date})")\n\ncomponent_result = course_participation.results(component="LAB1")[0]\ncomponent_result.set_grade("P", "2021-03-15")\ncomponent_result.finalize()\n```\n\n## More documentation\n\nThere are more detailed usage examples in the details documentation that can be \nround with the [releases][releases] and in the `examples` directory.\n\n[ladok]: https://start.ladok.se\n[docker]: https://hub.docker.com/repository/docker/dbosk/ladok3\n[releases]: https://github.com/dbosk/ladok3/releases\n\n\n# The examples\n\nThere are some examples that can be found in the `examples` directory:\n\n  - `example_LadokSession.py` just shows how to establish a session.\n  - `example_Course.py` shows course data related examples.\n  - `example_Student.py` shows student data related examples.\n  - `prgi.py` shows how to transfer grades from KTH Canvas to LADOK.\n  - `statsdata.py` shows how to extract data for doing statistics for a course \n    and the students\' results.\n\nWe also have a few more examples described in the sections below.\n\n## `canvas_ladok3_spreadsheet.py`\n\nPurpose: Use the data in a Canvas course room together with the data from Ladok3 to create a spreadsheet of students in the course\nand include their Canvas user_id, name, Ladok3 Uid, program_code, program name, etc.\n\nNote that the course_id can be given as a numeric value or a string which will be matched against the courses in the user\'s dashboard cards. It will first match against course codes, then short name, then original names.\n\nInput: \n```\ncanvas_ladok3_spreadsheet.py canvas_course_id\n```\nAdd the "-T" flag to run in the Ladok test environment.\n\nOutput: outputs a file (\'users_programs-COURSE_ID.xlsx) containing a spreadsheet of the users information\n\n```\ncanvas_ladok3_spreadsheet.py 12162\n\ncanvas_ladok3_spreadsheet.py -t \'II2202 HT20-1\'\n```\n\n\n## `ladok3_course_instance_to_spreadsheet.py`\n\nPurpose: Use the data in Ladok3 together with the data from Canvas to create a spreadsheet of students in a course\ninstance and include their Canvas user_id (or "not in Canvas" if they do not have a Canvas user_id), name, Ladok3 Uid, program_code, program name, etc.\n\nNote that the course_id can be given as a numeric value or a string which will be matched against the courses in the user\'s dashboard cards. It will first match against course codes, then short name, then original names.\n\nInput: \n```\nladok3_course_instance_to_spreadsheet.py course_code course_instance\n```\nor\n```\nladok3_course_instance_to_spreadsheet.py canvas_course_id\n```\nor\n```\n./ladok3_course_instance_to_spreadsheet.py course_code\n```\n\nOptionally include their personnumber with the flag -p or --personnumbers \n\nAdd the "-T" flag to run in the Ladok test environment.\n\nOutput: outputs a file (\'users_programs-instance-COURSE_INSTANCE.xlsx) containing a spreadsheet of the users information\n\n```\n# for II2202 the P1 instance in 2019 the course instance is 50287\nladok3_course_instance_to_spreadsheet.py II2202 50287\n```\nor\n```\n# Canvas course_id for II2202 in P1 is 20979\nladok3_course_instance_to_spreadsheet.py 20979\n```\nor\n```\n# P1P2 is a nickname on a dashboard card for II2202 duing P1 and P2\n./ladok3_course_instance_to_spreadsheet.py P1P2\n```\n\n\n## `canvas_students_missing_integration_ids.py`\n\nPurpose: Use the data in a Canvas course room to create a spreadsheet of students in the course who are missing an integration ID.\n\nInput: \n```\ncanvas_students_missing_integration_ids.py canvas_course_id\n```\nOutput: outputs a file (\'users_without_integration_ids-COURSE_ID.xlsx) containing a spreadsheet of the users information\n\n\n## `cl_user_info.py`\n\nPurpose: Use the data in a Canvas course room together with the data from Ladok3 to find information about a user.\n\nInput: \n```\nInput \ncl_user_info.py Canvas_user_id|KTHID|Ladok_id [course_id]\n```\nThe course_id can be a Canvas course_id **or** if you have dashboard cards, you can specific a course code, a nickname, unique part of the short name or original course name.\n\nAdd the "-k" or \'--kthid\' flag to get the KTHID (i.e., the \'sis_user_id) you need to specify a course_id for a course (where this user is a teacher or student) on the command line.\n\nAdd the "-T" flag to run in the Ladok test environment.\n\nIf you know the Ladok_id, i.e., the integration_id - then you do not need to specify a course_id.\n\nThe program can also take an argument in the form https://canvas.kth.se/courses/course_id/users/user_id\n- this is the URL when you are on a user\'s page in a course.\n\nOutput:\\\n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;from Canvas: sortable name, user_id, and integration_id\\\n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if you specified a course_id, you will also get KTHID and login_id\\\n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;from Ladok:  pnr (personnumber) and [program_code, program_name, specialization/track code, admissions info]\n\n\n',
    'author': 'Daniel Bosk',
    'author_email': 'dbosk@kth.se',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dbosk/ladok3',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
