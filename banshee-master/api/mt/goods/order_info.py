from api.mt.mt import Mt
import os
import datetime
from random import randint


class OrderInfo(Mt):
    method = 'get'
    api = '/v1/goods/$goods_id/order_info'
    data = {
        # 商品sku_id（不传递时会自动选择一个sku）
        # 'sku_id': '99937'
    }
    success_resp = {
        'code': 0
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }


    expected_schema = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "title": "expected_data",
        "type": "object",
        "required": ["code", "time", 'data'],
        "properties": {
            "code": {"type": "number"},
            "time": {"type": "number"},
            "data": {
                "type": "object",
                "required": ["bubble", 'bubble_position'],
                "properties": {
                    "bubble": {"type": "string"},
                    "bubble_position": {"type": "number"},
                }
            }
        }
    }
