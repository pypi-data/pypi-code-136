import re

import pytest
import responses

__version__ = "0.0.1"


@pytest.fixture
def idnow_responses(request=None):
    company_id = "yourcompany"
    with responses.RequestsMock(assert_all_requests_are_fired=False) as rsps:
        rsps.add(
            responses.POST,
            re.compile(
                f"https://gateway.test.idnow.de/api/v1/{company_id}/identifications/.*"
            ),
            json={"id": "new-idnow-id"},
            status=200,
        )
        yield rsps
