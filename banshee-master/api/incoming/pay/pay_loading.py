from locust import SequentialTaskSet, task
from api.incoming.pay.pay_order_query import PayOrderQuery

class PayLoading(SequentialTaskSet):
    @task
    def casepay_order_query(self):
        params = PayOrderQuery.loading_params()
        with self.client.post(params['url'], headers = params['headers'], data = params['data'], catch_response=True) as resp:
            if resp.json()['code'] == 0:
                resp.success()
            else:
                resp.failure("response 'code' should be 0")
    
    @task
    def faker_success(self):
        params = PayOrderQuery.loading_params()
        with self.client.post(params['url'], headers = params['headers'], data = params['data'], catch_response=True) as resp:
            if resp.json()['code'] == 60001:
                resp.success()
            elif resp.elapsed.total_seconds > 1:
                resp.failure("response took too long")
            else:
                resp.failure("response 'code' should be 60001")
