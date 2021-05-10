from api.mt.mt import Mt
import os
import datetime
from random import randint

 
class Trace(Mt):
    method = 'get'
    api = '/v1/refund/$refund_id/trace'
    data = {}

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
