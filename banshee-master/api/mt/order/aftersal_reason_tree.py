from api.mt.mt import Mt
import os
import datetime
from random import randint


class Reason_tree(Mt):
    method = 'post'
    api = '/v1/aftersale/reason_tree'
    data = {
        "order_id": "",
        "refund_id": "8529204803616686147"
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

