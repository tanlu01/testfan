from locust import SequentialTaskSet, task
import operator, random, string, logging
from load_testing.mt.loading_helper import mt_login, launch_loading
from api.mt.goods.goods import Goods
from api.mt.pay.payment_channel_status import PaymentChannelStatus

class BaseScenario(SequentialTaskSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x_token = ''
        self.goods_id = 107807

    @task
    def v1_goods(self):
        params = Goods.loading_params()
        # api = params['api'].replace('$goods_id', ''.join(random.choice(string.digits) for _ in range(6)))
        params['api'] = params['api'].replace('$goods_id', str(self.goods_id))
        launch_loading(self, params)
    
    @task
    def payment_channel_status(self):
        params = PaymentChannelStatus.loading_params()
        params['data']['goods_id'] = self.goods_id
        launch_loading(self, params)

    def on_start(self):
        self.x_token = mt_login()
    