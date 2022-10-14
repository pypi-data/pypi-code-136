# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pydantic


class SupplierReference(pydantic.BaseModel):
    """A reference to a **Supplier**."""
    id: int | None = pydantic.Field(
        default=None,
        title="Supplier ID",
        description=(
            "The supplier identifier as retained in Picqer. "
            "This property may be `null` if the **Supplier** is "
            "not maintained in Picqer."
        )
    )

    name: str = pydantic.Field(
        default=...,
        title="Name",
        description="The current name of the **Supplier**."
    )