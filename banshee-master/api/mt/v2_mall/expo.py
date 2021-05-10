from api.mt.mt import Mt
import os
import datetime
from random import randint


class Expo(Mt):
    method = 'get'
    api = "/v2/mall/100003/expo?product_information=$product_information"
    data = {}

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
