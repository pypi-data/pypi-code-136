import pytest
import requests
import responses
from btcpay_rest_client import BTCPayServerAPIClient

@pytest.fixture
def btcpay_url():
    yield "https://test-btcpay-api.com"

@pytest.fixture
def btcpay_store_id():
    # 44 character store id
    yield "12345678912345678912345678912345678912345678"

@pytest.fixture
def btcpay_auth_token():
    # 40 character API key
    yield "aabbccddeeaabbccddeeaabbccddeeaabbccddee"

@pytest.fixture
def btcpay_client(btcpay_url, btcpay_auth_token):
    client = BTCPayServerAPIClient.login_token(btcpay_url=btcpay_url, token=btcpay_auth_token)
    yield client

@responses.activate
def test_get_payment_request(btcpay_client, btcpay_url, btcpay_store_id):
    btcpay_client.set_store_id(btcpay_store_id)
    payment_request_id = "123456"
    test_url = f"{btcpay_url}/api/v1/stores/{btcpay_store_id}/payment-requests/{payment_request_id}"

    # configure the mock
    responses.add(
        responses.GET,
        test_url,
        json={
            "id": "123456",
            "status": "Pending",
            "created": 1592312018,
        },
        status=200
    )

    # run the function
    btcpay_client.get_payment_request(payment_request_id)

    # assert function runs correctly
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == test_url