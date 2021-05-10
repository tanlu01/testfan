from api.mt.mt import Mt
import os
import datetime
from random import randint


class Update_real_name(Mt):
    method = 'post'
    api = '/v1/order/$order_id/update_real_name'
    data = {
        "real_name_id": 0
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
