# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pydantic


class ProductReference(pydantic.BaseModel):
    """A reference to a **Product**."""
    id: int | None = pydantic.Field(
        default=None,
        title="Product ID",
        description="The product identifier as retained in Picqer. "
    )

    name: str = pydantic.Field(
        default=...,
        title="Name",
        description="The current name of the **Supplier**."
    )

    sku: str = pydantic.Field(
        default=...,
        title="SKU"
    )