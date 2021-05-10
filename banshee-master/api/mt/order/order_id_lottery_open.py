from api.mt.mt import Mt
import os
import datetime
from random import randint


class Lottery_Open(Mt):
    method = 'post'
    api = '/v1/order/$order_id/lottery/open'
    data = {}

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
