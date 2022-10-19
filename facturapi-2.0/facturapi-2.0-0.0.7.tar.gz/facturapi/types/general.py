from typing import List, Optional
import datetime as dt

from pydantic import BaseModel

from .validators import sanitize_dict
from .enums import Steps


class CustomerAddress(BaseModel):
    """Address of a customer.

    Attributes:
        street (str): Street.
        exterior (str): Exterior place number.
        interior (str): Interior place number.
        neighborhood (str): 'Colonia'.
        city (str): City.
        municipality (str): 'Municipio or Alcaldía'.
        state (str): State of the address.
        zip (str): Postal code.
        country (str): Country.

    """

    street: Optional[str]
    exterior: Optional[str]
    interior: Optional[str]
    neighborhood: Optional[str]
    city: Optional[str]
    municipality: Optional[str]
    zip: Optional[str]
    state: Optional[str]
    country: Optional[str]

class Taxes(BaseModel):
    """Taxes basic info."""
    rate: float = 0.16
    type: str = "IVA"
    factor: Optional[str] = "Tasa"
    withholding : Optional[bool] = False

class LocalTaxes(BaseModel):
    """Local taxes info"""
    rate: float
    type: str
    withholding : Optional[bool] = False


class CustomerBasicInfo(BaseModel):
    """Customer's basic info"""

    id: str
    legal_name: str
    tax_id: str
    tax_system: str


class ItemPart(BaseModel):
    """Defines a part of an invoice item."""

    description: str
    product_key: str
    quantity: Optional[int] = 1
    sku: Optional[str]
    unit_price: Optional[float]
    customs_keys: Optional[List[str]]


class Namespace(BaseModel):
    """Namespace for spceial XML namespaces for an invoice."""

    prefix: Optional[str]
    uri: Optional[str]
    schema_location: Optional[str]


class ProductBasicInfo(BaseModel):
    """Product's basic info."""

    id: Optional[str]
    description: str
    product_key: str
    price: int
    tax_included: Optional[bool] = False
    taxability: Optional[str] = "01"
    taxes : Optional[List[Taxes]] = None
    local_taxes : Optional[LocalTaxes] = None
    unit_key: Optional[str]
    unit_name: Optional[str]

class InvoiceDocuments(BaseModel):
    relationship : str
    documents : List

class InvoiceStamp(BaseModel):
    signature : str
    date : dt.datetime
    sat_cert_number: str
    sat_signature: str

class PendingSteps(BaseModel):
    type: Optional[Steps]
    description : str

class Legal(BaseModel):
    name: str
    legal_name: str
    tax_system: Optional[str]
    website: Optional[str]
    phone: Optional[str]

class SanitizedDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        sanitize_dict(self)

class OrganizationAddress(BaseModel):
    """Address of an organization.

    Attributes:
        zip (str): Postal code.
        street (str): Street.
        exterior (str): Exterior place number.
        interior (str): Interior place number.
        neighborhood (str): 'Colonia'.
        city (str): City.
        municipality (str): 'Municipio or Alcaldía'.
        state (str): State of the address.
    """

    zip: str
    street: str
    exterior: str
    interior: Optional[str]
    neighborhood: Optional[str]
    city: Optional[str]
    municipality: Optional[str]
    state: Optional[str]




