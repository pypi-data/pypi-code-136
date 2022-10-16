"""Mocks used for testing."""

import httmock

# Kalabash API mocks


@httmock.urlmatch(
    netloc=r"api\.kalabash\.org$", path=r"^/1/instances/search/", method="post")
def kalmonak_api_instance_search(url, request):
    """Return empty response."""
    return {"status_code": 404}


@httmock.urlmatch(
    netloc=r"api\.kalabash\.org$", path=r"^/1/instances/", method="post")
def kalmonak_api_instance_create(url, request):
    """Simulate successful creation."""
    return {
        "status_code": 201,
        "content": {"pk": 100}
    }


@httmock.urlmatch(
    netloc=r"api\.kalabash\.org$", path=r"^/1/instances/.+/", method="put")
def kalmonak_api_instance_update(url, request):
    """Simulate successful update."""
    return {"status_code": 200}


@httmock.urlmatch(
    netloc=r"api\.kalabash\.org$", path=r"^/1/versions/", method="get")
def kalmonak_api_versions(url, request):
    """Simulate versions check."""
    return {
        "status_code": 200,
        "content": [
            {"name": "kalabash", "version": "9.0.0", "url": ""},
        ]
    }


@httmock.urlmatch(
    netloc=r"api\.kalabash\.org$", path=r"^/1/versions/", method="get")
def kalmonak_api_versions_no_update(url, request):
    """Simulate versions check."""
    return {
        "status_code": 200,
        "content": [
            {"name": "kalabash", "version": "0.0.0", "url": ""},
        ]
    }
