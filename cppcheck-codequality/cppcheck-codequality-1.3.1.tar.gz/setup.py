# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cppcheck_codequality']

package_data = \
{'': ['*']}

install_requires = \
['xmltodict>=0.13.0,<0.14.0']

entry_points = \
{'console_scripts': ['cppcheck-codequality = '
                     'cppcheck_codequality.__main__:main']}

setup_kwargs = {
    'name': 'cppcheck-codequality',
    'version': '1.3.1',
    'description': 'Convert a CppCheck XML report to a GitLab-compatible Code Quality JSON report.',
    'long_description': '# cppcheck-codequality\n\n[![badge-pypi](https://img.shields.io/pypi/v/cppcheck-codequality.svg?logo=pypi)](https://pypi.python.org/pypi/cppcheck-codequality/)\n&nbsp;\n[![badge-pypi-downloads](https://img.shields.io/pypi/dm/cppcheck-codequality)](https://pypi.org/project/cppcheck-codequality/)\n\n\n[![badge-pipeline](https://gitlab.com/ahogen/cppcheck-codequality/badges/main/pipeline.svg)](https://gitlab.com/ahogen/cppcheck-codequality/-/pipelines?scope=branches)\n&nbsp;\n[![badge-coverage](https://gitlab.com/ahogen/cppcheck-codequality/badges/main/coverage.svg)](https://gitlab.com/ahogen/cppcheck-codequality/-/pipelines?scope=branches)\n&nbsp;\n[![badge-pylint](https://gitlab.com/ahogen/cppcheck-codequality/-/jobs/artifacts/main/raw/badge.svg?job=pylint)](https://gitlab.com/ahogen/cppcheck-codequality/-/pipelines?scope=branches)\n&nbsp;\n[![badge-formatting](https://gitlab.com/ahogen/cppcheck-codequality/-/jobs/artifacts/main/raw/badge.svg?job=format_black)](https://gitlab.com/ahogen/cppcheck-codequality/-/pipelines?scope=branches)\n&nbsp;\n[![badge-issues-cnt](https://img.shields.io/badge/dynamic/json?label=issues&query=statistics.counts.opened&url=https%3A%2F%2Fgitlab.com%2Fapi%2Fv4%2Fprojects%2F19114200%2Fissues_statistics%3Fscope%3Dall)](https://gitlab.com/ahogen/cppcheck-codequality/-/issues)\n\n\n## About\n\nI wanted reports from CppCheck to appear in GitLab Merge Requests as [Code\nQuality reports](https://docs.gitlab.com/ee/user/project/merge_requests/code_quality.html#implementing-a-custom-tool),\nwhich is a JSON file defined by the Code Climate team/service.\n\nThat\'s all this does: convert CppCheck XML to Code Climate JSON.\n\n### Usage\n\nIt is primarily used as a console script. As such, ensure you have Python 3\'s "scripts" directory in your `PATH` variable.\nFor example, on Linux, that might be `$HOME/.local/bin`.\n\nTo test, try the `--help` or `--version` flags:\n```bash\ncppcheck-codequality --help\n```\n\nCppCheck already has a script to convert its XML report to HTML for easy\nhuman reading. See "Chapter 11 HTML Report" in the [CppCheck Manual](http://cppcheck.sourceforge.net/manual.pdf)\n\nThis script follows that example and provides similar command-line options.\nA typical workflow might look like this:\n\n```bash\n# Generate CppCheck report as XML\ncppcheck --xml --enable=warning,style,performance ./my_src_dir/ 2> cppcheck_out.xml\n# Convert to a Code Climate JSON report\ncppcheck-codequality --input-file cppcheck_out.xml --output-file cppcheck.json\n```\n\nIf you wanted, you could invoke the script directly as a module, like this:\n\n```bash\n# Run as a module instead (note the underscore in the module name here)\npython -m cppcheck_codequality --input-file=cppcheck_out.xml --output-file=cppcheck.json\n```\n\nNow, in your GitLab CI script, [upload this file](https://docs.gitlab.com/ee/ci/pipelines/job_artifacts.html#artifactsreportscodequality)\nas a Code Quality report.\n\n```yaml\nmy-code-quality:\n  script:\n    - [...]\n  artifacts:\n    reports:\n      codequality: cppcheck.json\n```\n\n### Contributing\n\n* Sign the contributor agreement (coming soon)\n* Format with [black](https://pypi.org/project/black/)\n* Check with [pylint](https://pypi.org/project/pylint/)\n\n### Credits & Trademarks\n\nCppCheck is an open-source project with a GPL v3.0 license.\n* http://cppcheck.sourceforge.net\n* https://github.com/danmar/cppcheck\n\n"Code Climate" may be a registered trademark of Code Climate, Inc. which provides\nsuper-cool free and paid services to the developer community.\n* https://codeclimate.com\n* https://github.com/codeclimate\n\n"GitLab" is a trademark of GitLab B.V.\n* https://gitlab.com\n* https://docs.gitlab.com/ee/user/project/merge_requests/code_quality.html\n\nAll other trademarks belong to their respective owners.\n',
    'author': 'Alex Hogen',
    'author_email': 'code.ahogen@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/ahogen/cppcheck-codequality',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.8,<=3.11',
}


setup(**setup_kwargs)
