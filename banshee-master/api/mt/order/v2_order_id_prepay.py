from api.mt.mt import Mt
import os
import datetime
from random import randint


class V2_Prepay(Mt):
    method = 'post'
    api = '/v2/order/$order_id/prepay'
    data = {
        "platform": 50,      #android app
        "payment_method": 9  #支付方式0-9,11,12,18.18
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
