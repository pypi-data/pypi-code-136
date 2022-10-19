from dataclasses import dataclass
import datetime


@dataclass
class BTAImport:
    _1: int
    _2: int
    _3: int
    _4: int
    company: str
    account: int
    line_description: str
    division: str
    branch: str
    product: str
    other: str
    function: str
    employee: str
    n___a_1: str
    n___a_2: str
    amount: float
    accounting_date: datetime.datetime
    ratedate: datetime.datetime
    site: str
    journal_description: str
    bpr: str
    control_account: str
    currency: str
    tax: str
