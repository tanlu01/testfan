from api.mt.mt import Mt
import os
import datetime
from random import randint


class Mall_middle_page(Mt):
    method = 'get'
    api = '/v2/search/mall/hotWords?mallId=$mall_id'
    data = {}

    success_resp = {
        'code': 0
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
    word=[
        "垃圾袋","水果", "大米", "手表", "零食", "牙膏", "泡面", "旺仔牛奶", "蓝牙耳机", "小龙虾","内裤男", "自热火锅"
    ]


