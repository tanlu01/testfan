from api.mt.mt import Mt
import os
import datetime
from random import randint


class V1_Order_id_Cancel(Mt):
    method = 'post'
    api = '/v1/order/$order_id/cancel'
    data = {}

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
