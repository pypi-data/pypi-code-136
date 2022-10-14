# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pydantic

from .productreference import ProductReference


class PurchasedProduct(pydantic.BaseModel):
    """Represents a **Product** that is purchased and expected to
    be delivered.
    """
    order_id: int = pydantic.Field(
        default=...,
        title="Order ID",
        description="A reference to the order with which this product was ordered."
    )

    product: ProductReference = pydantic.Field(
        default=...,
        title="Product",
        description="A reference to the **Product** that was ordered."
    )

    amount: int = pydantic.Field(
        default=0,
        title="Amount",
        description="The expected delivery amount."
    )

    delivered: int = pydantic.Field(
        default=0,
        title="Delivered",
        description="The amount that is delivered."
    )