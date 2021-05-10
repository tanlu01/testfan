from api.mt.mt import Mt
import os
import datetime
from random import randint


class Revoke(Mt):
    method = 'post'
    api = '/v1/refund/$refund_id/revoke'
    data = {}

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
