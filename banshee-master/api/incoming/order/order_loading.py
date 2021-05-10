from locust import SequentialTaskSet, task
from api.incoming.order.create import Create

class OrderLoading(SequentialTaskSet):
    @task
    def create(self):
        params = Create.loading_params()
        with self.client.post(params['url'], headers = params['headers'], data = params['data'], catch_response=True) as resp:
            if resp.json()['code'] == 0:
                resp.success()
            else:
                resp.failure("response 'code' should be 0")

    @task
    def fake_success_create(self):
        params = Create.loading_params()
        with self.client.post(params['url'], headers = params['headers'], data = params['data'], catch_response=True) as resp:
            if resp.json()['code'] == 65004:
                resp.success()
            else:
                resp.failure("response 'code' should be 0")

