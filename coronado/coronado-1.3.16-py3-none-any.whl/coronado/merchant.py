# vim: set fileencoding=utf-8:

import json
import logging

from coronado import TripleObject
from coronado.address import Address
from coronado.baseobjects import BASE_MERCHANT_DICT, BASE_MERCHANT_LOCATION_DICT
from coronado.exceptions import InvalidPayloadError, CallError
from coronado.merchantcodes import MerchantCategoryCode
# +++ constants +++

SERVICE_PATH = 'partner/merchants'
"""
The default service path associated with Merchant operations.

Usage:

```python
Merchant.initialize(serviceURL, SERVICE_PATH, auth)
```

Users are welcome to initialize the class' service path from regular strings.
This constant is defined for convenience.
"""


# *** classes and objects ***


# --- globals ---

log = logging.getLogger(__name__)


class MerchantLocation(TripleObject):
    """
    A merchant's business adddress, whether physical or on-line.

    See `coronado.address.Address`
    """

    requiredAttributes = [
        'address',
        'objID',
    ]

    def __init__(self, obj = BASE_MERCHANT_LOCATION_DICT):
        """
        Create a new MerchantLocation instance.
        """
        TripleObject.__init__(self, obj)


    @classmethod
    def create(klass, **args) -> object:
        """
        **Disabled for this class.**
        """
        None


    @classmethod
    def byID(klass, objID: str) -> object:
        """
        **Disabled for this class.**
        """
        None


    @classmethod
    def updateWith(klass, objID: str, spec: dict) -> object:
        """
        **Disabled for this class.**
        """
        None


    @classmethod
    def list(klass, paramMap = None, **args) -> list:
        """
        **Disabled for this class.**
        """
        None


class Merchant(TripleObject):
    """
    Merchant is a company or person involved in trade, most often retail, that
    processes card payments as a result of that trade.
    """
    requiredAttributes = [
        'address',
        'assumedName',
        'createdAt',
        'merchantCategory',
        'updatedAt',
    ]
    allAttributes = TripleObject(BASE_MERCHANT_DICT).listAttributes()


    def __init__(self, obj = BASE_MERCHANT_DICT):
        """
        Create a new Merchant instance.
        """
        TripleObject.__init__(self, obj)


    @classmethod
    def create(klass, 
                address: Address,
                assumedName: str,
                merchantCategoryCode: str,
                extMerchantID: str,
                logoURL: str = None) -> object:
        """
        Creates a merchant and returns an instance of the new object.

        Arguments
        ---------

            extMerchantID: str
        The external, non-triple merchant ID

            address: Address
        An instance of `coronado.address.Address` initialized to the merchant's
        physical address

            assumedName: str
        The merchant's assumed name

            logoURL: string
        A URL to the merchant's logo.

            merchantCategoryCode: MerchantCategoryCode
        The 4-digit standardized merchant category code (MCC).  See
        `coronado.merchantcodes.MerchantCategoryCode` for a full list.

        Returns
        -------

        An instance of `Merchant` if it was created by the triple back-end,, or
        `None`.

        Raises
        ------
            CoronadoError
        A CoronadoError dependent on the specific error condition.  The full list of
        possible errors, causes, and semantics is available in the
        **`coronado.exceptions`** module.
        """
        spec = {
            'address': address.asSnakeCaseDictionary(),
            'assumed_name': assumedName,
            'external_id': extMerchantID,
            'logo_url': logoURL,
            'merchant_category_code': merchantCategoryCode,
        }
        merchant = super().create(spec)
        #Convert TripleObject to Address
        merchant.address = Address(merchant.address) 
        #Convert TripleObject to MerchantCategoryCode
        merchant.merchantCategory = MerchantCategoryCode(merchant.merchantCategory) 
        return merchant
        #return Merchant(super().create(spec))

    @classmethod
    def list(klass: object, paramMap = None, **args) -> list:
        """
        List all merchants that match any of the criteria set by the
        arguments to this method.

        Arguments
        ---------
            externalMerchantID
        String, 1-50 characters partner-provided external ID

        Returns
        -------
            list
        A list of Merchant objects; can be `None`.
        """
        paramMap = {
            'externalMerchantID': 'merchant_external_id',
        }
        response = super().list(paramMap, **args)
        result = [ TripleObject(obj) for obj in json.loads(response.content)['merchants'] ]
        return result


    @classmethod
    def byID(klass, objID: str) -> object:
        merchant = super().byID(objID)
        # Convert TripleObject to Address
        if not merchant:
            return None
        merchant.address = Address(merchant.address) 
        # Convert TripleObject to MerchantCategoryCode
        merchant.merchantCategory = MerchantCategoryCode(merchant.merchantCategory) 
        return merchant

    @classmethod
    def updateWith(klass, objID : str, spec : dict) -> object:
        merchant = super().updateWith(objID,spec)
        if not merchant:
            raise InvalidPayloadError('The specified Merchant cannot be found to update')
        # Convert TripleObject to Address
        merchant.address = Address(merchant.address) 
        # Convert TripleObject to MerchantCategoryCode
        merchant.merchantCategory = MerchantCategoryCode(merchant.merchantCategory) 
        return merchant


