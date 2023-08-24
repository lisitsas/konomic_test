import pytest
import requests
import logging

logger = logging.getLogger("test")


@pytest.mark.parametrize('limit', [1, 100, 500, 1000, 5000])
def test_get_api_v3_depth(limit):
    symbol = 'ETHBTC'
    url = f"https://testnet.binance.vision/api/v3/depth?symbol={symbol}&limit={limit}"
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get(
        url=url, headers=headers, auth=None)
    logging.info(response.json())
    assert response.status_code == 200
    assert response.json().get('lastUpdateId') != None
    assert isinstance(response.json().get('lastUpdateId'), int)
    assert response.json().get('bids') != []
    assert isinstance(response.json().get('bids'), list)
    assert response.json().get('bids')[0] != []
    assert isinstance(response.json().get('bids')[0], list)
    assert response.json().get('bids')[0][0] != None
    assert isinstance(response.json().get('bids')[0][0], str)
    assert response.json().get('bids')[0][1] != None
    assert isinstance(response.json().get('bids')[0][1], str)
    assert isinstance(response.json().get('bids')[0], list)
    assert response.json().get('asks') != []
    assert isinstance(response.json().get('asks'), list)
    assert response.json().get('asks')[0] != []
    assert isinstance(response.json().get('asks')[0], list)
    assert response.json().get('asks')[0][0] != None
    assert isinstance(response.json().get('asks')[0][0], str)
    assert response.json().get('asks')[0][1] != None
    assert isinstance(response.json().get('asks')[0][1], str)
