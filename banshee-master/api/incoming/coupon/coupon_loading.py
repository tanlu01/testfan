from locust import SequentialTaskSet, task
from api.incoming.coupon.batch_issue import BatchIssue
from api.incoming.coupon.save_coupon_group import SaveCouponGroup

class CouponLoading(SequentialTaskSet):
    @task
    def batch_issue(self):
        params = BatchIssue.loading_params()
        with self.client.post(params['url'], headers = params['headers'], data = params['data'], catch_response=True) as resp:
            if resp.json()['code'] == 0:
                resp.success()
            else:
                resp.failure("response 'code' should be 0")

    @task
    def faker_success_batch_issue(self):
        params = BatchIssue.loading_params()
        with self.client.post(params['url'], headers = params['headers'], data = params['data'], catch_response=True) as resp:
            if resp.json()['code'] == 62003:
                resp.success()
            else:
                resp.failure("response 'code' should be 0")   

    @task
    def save_coupon_group(self):
        params = SaveCouponGroup.loading_params()
        with self.client.post(params['url'], headers = params['headers'], data = params['data'], catch_response=True) as resp:
            if resp.json()['code'] == 0:
                resp.success()
            else:
                resp.failure("response 'code' should be 0")
