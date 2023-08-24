# Konomic Test Task

## Install requirements

- `python -m venv venv`
- `venv\Scripts\activate.bat`
- `pip install -r requirements.txt`

## 1.1 Order book for ETHBTC

`pytest test_binance_api.py`

## 1.2 P95 latency measurement

Criteria:

- P95 <= 500ms - test passed
- P95 > 500ms - test failed

`locust -f locustfile.py -u 10 -t 10 --headless -i 100`

Example:

![P95](pics/image.png)

## 2 Search on habr.com

Criteria:

- status code == 200 OK - test passed
- status code != 200 OK - test failed

`pytest test_habr.py`
