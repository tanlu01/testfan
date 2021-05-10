from locust import SequentialTaskSet, task
from api.incoming.coin.get_account_coin import GetAccountCoin
from api.incoming.coin.new_coin import NewCoin

class CoinLoading(SequentialTaskSet):
    @task
    def get_account_coin(self):
        params = GetAccountCoin.loading_params()
        with self.client.get(params['url'], headers = params['headers'], params = params['data'], catch_response=True) as resp:
            if resp.json()['code'] == 0:
                resp.success()
            else:
                resp.failure("response 'code' should be 0")

    @task
    def new_coin(self):
        params = NewCoin.loading_params()
        with self.client.post(params['url'], headers = params['headers'], data = params['data'], catch_response=True) as resp:
            if resp.json()['code'] == 0:
                resp.success()
            else:
                resp.failure("response 'code' should be 0")


