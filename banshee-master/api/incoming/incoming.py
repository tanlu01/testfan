import time, datetime
from random import randint
from api.request import Request
from api.encrypt import incoming_sign


class Incoming(Request):
    pay = {
        "land": "0",
        "open_id": "123",
        "amount": 100,
        "ishidetitle": "undefined",
        "mid": "271813449",
        "app_id": "bteevncrky5n",
        "notice_url": "https://newidea4-gamecenter-backend.1sapp.com/x/pay/notice",
        "extra": "{\"money\":100,\"openId\":\"123\",\"appId\":\"a3AShXuKqBfY\",\"platform\":\"qtt\",\"gameName\":\"undefined\",\"notifyUrl\":\"https://newidea4-gamecenter-backend.1sapp.com/x/game-center/user/game-coin/callback\",\"source\":\"286100\",\"ext\":\"{\\\"transaction_id\\\":\\\"202001-8f2b6f6e-5261-4fd7-b2c2-3bf5beed6cec\\\"}\",\"land\":\"0\",\"tuid\":\"XahEjEgcn6m2efV7g--B2g\"}",
        "pl": "qtt",
        "user_type": "13",
        "channel_scene_id": 0,
        "title": "游戏中心",
        "scene_id": 1,
        "from": "H5",
        "receipt": 1,
        "channels": [{
            "id": 2,
            "amount": 100,
            "currency": "cny"
        }],
        "out_trade_no": datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "-union-qtt-" + str(randint(0, 99999)),
        "quit_url": "https://qttpay.1sapp.com/pay2",
        "return_url": "https://qttpay.1sapp.com/pay2"
    }

    coupon = {
        "app_id": "",
        "user_id": "",
        "user_type": "",
        "product_id": "",
        "product_price": "",
        "coupon_code": ""
    }

    def request(self):
        # 如果data['token']是空，就走加密服务，无需签名。
        if self.data.get('token') is not None:
            sign = incoming_sign(params=self.data, ingnored_keys=('sign', 'token', 'timestamp'), filter_falsy=True)
            self.data['sign'] = sign
        return super().request()
