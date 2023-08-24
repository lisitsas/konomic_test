from locust import FastHttpUser, task


class BinanceUser(FastHttpUser):

    host = 'https://testnet.binance.vision'

    @task
    def get_depth_100(self):
        symbol = 'ETHBTC'
        limit = 100
        url = f"/api/v3/depth?symbol={symbol}&limit={limit}"
        response = self.client.get(url=url)

    @task
    def get_depth_500(self):
        symbol = 'ETHBTC'
        limit = 500
        url = f"/api/v3/depth?symbol={symbol}&limit={limit}"
        response = self.client.get(url=url)

    @task
    def get_depth_1000(self):
        symbol = 'ETHBTC'
        limit = 1000
        url = f"/api/v3/depth?symbol={symbol}&limit={limit}"
        response = self.client.get(url=url)

    @task
    def get_depth_5000(self):
        symbol = 'ETHBTC'
        limit = 5000
        url = f"/api/v3/depth?symbol={symbol}&limit={limit}"
        response = self.client.get(url=url)
