from dotenv import load_dotenv
load_dotenv()
load_dotenv(verbose=True)
from pathlib import Path
env_path = Path('env/default') / 'qtt.properties'
load_dotenv(dotenv_path=env_path)

from locust import HttpUser, task, tag, between, constant, events
from api.incoming.pay.pay_loading import PayLoading
from api.incoming.coin.coin_loading import CoinLoading
from api.incoming.coupon.coupon_loading import CouponLoading
from api.incoming.order.order_loading import OrderLoading

class PayLoading(HttpUser):
    wait_time = between(1, 2)
    host = ''
    
    # tasks = {DummyLoading: 1}
    tasks = {PayLoading: 1 ,CoinLoading: 1, CouponLoading: 1, OrderLoading: 1}

    @events.request_success.add_listener
    def my_success_handler(self, request_type, name, response_time, response_length, **kw):
        pass