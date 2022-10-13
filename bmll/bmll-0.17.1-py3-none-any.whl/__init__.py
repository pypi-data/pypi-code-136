"""
#### Authentication

You will need to configure the following environment variables prior to importing `bmll`:


* `BMLL_KEY_PATH`: api private key path
* `BMLL_KEY_PASSPHASE`: (optional) the passphrase for the key if exists.
* `BMLL_USERNAME`: (optional) [api username](https://data.bmlltech.com/#app/api-access).
        will attempt to read this from the public key comment unless provided.


or call:


```python
bmll.login(username, key_path, passphrase)
```

For lab services, you should also pass-in your lab organisation ID:

```python
bmll.login(username, key_path, passphrase, lab_org_id)
```


Examples:

    ```python
    bmll.reference.query(Ticker='VOD')
    ```

    ```python
    bmll.reference.query(MIC='XLON')
    ```

    ```python
    bmll.time_series.query(Ticker='VOD',
                           MIC='XLON',
                           metric='TradeCount',
                           freq='D',
                           start_date='2019-06-24',
                           end_date='2019-12-31')
    ```

    ```python
    bmll.time_series.query(Ticker=['VOD', 'RDSA'],
                           MIC='XLON',
                           metric={
                               'metric': 'TradeCount',
                               'tags.Classification': 'LitAddressable'
                           },
                           freq='D',
                           start_date='2019-06-24',
                           end_date='2019-12-31')
    ```

"""
from bmll import account
from bmll import compute
from bmll import market_data
from bmll import reference
from bmll import time_series
from bmll import exceptions
from bmll._rest import login, logout, Session

__all__ = (
    "__author__",
    "__contact__",
    "__homepage__",
    "__version__",
    "account",
    "compute",
    "market_data",
    "reference",
    "time_series",
    "exceptions",
    "login",
    "logout",
    "Session"
)


def __get_meta():
    import json
    import pathlib
    f = pathlib.Path(__file__).parent / "_metadata.json"
    return json.loads(f.read_text())


_meta = __get_meta()


__author__ = _meta["author"]
__contact__ = __author__
__homepage__ = _meta["url"]
__version__ = _meta["version"]
