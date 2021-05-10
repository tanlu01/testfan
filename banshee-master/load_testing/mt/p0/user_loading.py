from locust import SequentialTaskSet, task
import operator
from api.mt.user.login import Login
from api.mt.user.prime import Prime

class UserLoading(SequentialTaskSet):
    @task
    def login(self):
        params = Login.loading_params()
        # with self.client.get(params['url'], headers = params['headers'], json = params['data'], catch_response=True) as resp:
        with operator.methodcaller(params['method'], params['url'], headers = params['headers'], json = params['data'], catch_response=True)(self.client) as resp:
            if resp.json()['code'] == 0:
                resp.success()
            else:
                resp.failure(f"response 'code' should be 0. {resp.json()}")
    
    @task
    def prime(self):
        params = Prime.loading_params()
        with operator.methodcaller(params['method'], params['url'], headers = params['headers'], json = params['data'], catch_response=True)(self.client) as resp:
            if resp.json()['code'] == 0:
                resp.success()
            else:
                resp.failure(f"response 'code' should be 0. {resp.json()}")
            
    