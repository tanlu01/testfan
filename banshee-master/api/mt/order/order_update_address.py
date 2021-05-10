from api.mt.mt import Mt
import os
import datetime
from random import randint


class Update_address(Mt):
    method = 'post'
    api = '/v1/order/$order_id/update_address'
    data = {
        "address_id": 0
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
