# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import aorta
import pydantic

from ..purchaser import Purchaser
from ..purchasedproduct import PurchasedProduct
from ..supplierreference import SupplierReference
from ..warehousereference import WarehouseReference


class PurchaseOrderPurchased(aorta.Event):
    id: int = pydantic.Field(
        default=...,
        title="Purchase Order ID",
        description="The Picqer ID of the **Purchase Order**."
    )

    ref: str = pydantic.Field(
        default=...,
        title="Reference",
        description=(
            "The **Purchase Order** number as defined by the procurement "
            "system."
        )
    )

    supplier: SupplierReference = pydantic.Field(
        default=...,
        title="Supplier",
        description=(
            "Describes the **Supplier** with which the **Purchase Order** "
            "was placed."
        )
    )

    supplier_document_id: str | None = pydantic.Field(
        default=None,
        title="Supplier Document ID",
        description=(
            "A document ID retained by the **Supplier** for this specific "
            "**Purchase Order**, such as an order or invoice number."
        )
    )

    warehouse: WarehouseReference = pydantic.Field(
        default=...,
        title="Warehouse",
        description=(
            "The **Warehouse** to which the goods included in the **Purchase "
            "Order** are expected to be shipped."
        )
    )

    purchaser: Purchaser = pydantic.Field(
        default=...,
        title="Purchaser",
        description=(
            "The person that placed the **Purchase Order** with the "
            "**Supplier**."
        )
    )

    products: list[PurchasedProduct] = pydantic.Field(
        default=...,
        title="Products",
        description="The list of products that were ordered."
    )