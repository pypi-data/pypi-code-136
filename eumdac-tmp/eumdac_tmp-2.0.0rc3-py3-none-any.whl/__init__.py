"""
Eumidas Library
~~~~~~~~~~~~~~~
Eumidas is a Python library to simplify the access to Eumetsat Data Services.
Basic DataStore usage:
   >>> from eumdac.token import AccessToken
   >>> from eumdac.datastore import DataStore
   >>> consumer_key = 'my-consumer-key'
   >>> consumer_secret = 'my-consumer-secret'
   >>> credentials = (consumer_key, consumer_secret)
   >>> token = token = AccessToken(credentials)
   >>> datastore = DataStore(token)
   >>> for collection in datastore.collections:
   ...     print(f"{collection} - {collection.title}")
   ...
   EO:EUM:DAT:MSG:HRSEVIRI - High Rate SEVIRI Level 1.5 Image Data - MSG - 0 degree
   EO:EUM:DAT:MSG:MSG15-RSS - Rapid Scan High Rate SEVIRI Level 1.5 Image Data - MSG
   EO:EUM:DAT:0080 - MVIRI Level 1.5 Climate Data Record - MFG - 0 degree
   EO:EUM:DAT:MSG:RSS-CLM - Rapid Scan Cloud Mask - MSG
   EO:EUM:DAT:0081 - MVIRI Level 1.5 Climate Data Record - MFG - 57 degree
   ...
"""
from .__version__ import (
    __author__,
    __author_email__,  # noqa
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
)
from .datastore import DataStore  # noqa
from .datatailor import DataTailor  # noqa
from .token import AccessToken  # noqa
