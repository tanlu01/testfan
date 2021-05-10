from api.mt.mt import Mt
import os
import datetime
from random import randint


class Activate(Mt):
    method = 'post'
    api = '/v1/cash_card/activate'
    data = {
        "card_secret": "string"
    } 

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
