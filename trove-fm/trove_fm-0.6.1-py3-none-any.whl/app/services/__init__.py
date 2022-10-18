
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


from trove_fm.app.services.authentication import AuthService
from trove_fm.app.services.email import EmailService
from trove_fm.app.services.security import NewAccountVerificationService
from trove_fm.app.services.oauth2 import OAuth2PasswordBearerSecure  # noqa

auth_service = AuthService()
verification_service = NewAccountVerificationService()
email_service = EmailService()
