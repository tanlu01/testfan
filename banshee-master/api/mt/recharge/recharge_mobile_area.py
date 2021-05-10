from api.mt.mt import Mt
import os
import datetime
from random import randint


class Mobile_area(Mt):
    method = 'get'
    api = '/v1/recharge/mobile_area'
    data = {}


    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
