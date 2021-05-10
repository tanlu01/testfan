from api.mt.mt import Mt
import os
import datetime
from random import randint


class Captcha_picture(Mt):
    method = 'get'
    api = '/v1/captcha_picture'
    data = {}

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
