from api.mt.mt import Mt
import os
import datetime
from random import randint


class Order_check(Mt):
    method = 'post'
    api = '/v1/recharge/order_check'
    data = {
        "coupon_id": "string",
        "recharge_id": 0,
        "recv_target": "string",
        "recv_type": 0,
        "use_cash_card": True
    }
    #参数添加无信息

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
