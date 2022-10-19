from subprocess import run


def _run(cmd: str) -> None:
    run(cmd, shell=True)


_run("touch TEST_MYPANDAS_OUTPUT")
_run("py ./tests/test_mypandas.py > TEST_MYPANDAS_OUTPUT")

README = f"""\
# qpandas


---


WORK IN PROGRESS


---


Query Panadas DataFrames with SQL


## Install

Currently available on [PyPI](https://pypi.org/project/qpandas/), to install:
```
pip install qpandas
```

## Example

```py
{''.join(open('./tests/test_mypandas.py').readlines())}```
```
{open('TEST_MYPANDAS_OUTPUT').read()}```

### Example explanation
The `URL` variable is a database URL, for my information about URL formatting including passwords with special characters [click here](https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls). In this example, the default MySQL username and password for [Github Action's runner images](https://github.com/actions/runner-images) is used.

Also notice that `locals()` is passed when an initialized `MyPandas` object is `__call__`'ed, which provides the current scope's local variables. That is how MyPandas is able to query the Pandas DataFrames in the current scope based on just a string. When `__call__`'ing an initialized `MyPandas` object from within a function, pass `globals()` instead if you need to query DataFrames in the global scope.
"""

_run("rm TEST_MYPANDAS_OUTPUT")


if __name__ == "__main__":
    with open("README.md", "w") as f:
        f.write(README)
