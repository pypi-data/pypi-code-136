
"""
TroveFM is an online store and headless CMS.

Copyright (C) 2022  Brian Farrell

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: brian.farrell@me.com
"""


from fastapi import APIRouter

from trove_fm.app.api.routes.company import router as company_router
from trove_fm.app.api.routes.ping import router as ping_router
from trove_fm.app.api.routes.person import router as person_router

router = APIRouter()


# The order that these routes are added here will be reflected in the order that they are
# displayed in the API documentation at the /docs/ endpoint.
router.include_router(ping_router, tags=["ping"])
router.include_router(company_router, prefix="/company", tags=["company"])
router.include_router(person_router, prefix="/person", tags=["person"])
