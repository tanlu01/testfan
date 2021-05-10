from api.mt.mt import Mt
import os
import datetime
from random import randint


class Sign(Mt):
    method = 'post'
    api = '/v1/order/$order_id/sign'
    data = {

    }
    success_resp={
        "code":0
    }
    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
