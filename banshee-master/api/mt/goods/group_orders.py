from api.mt.mt import Mt
import os
import datetime
from random import randint


class Group_orders(Mt):
    method = 'get'
    api = '/v1/goods/$goods_id/group_orders'
    data = {}

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
                "required": ["total", 'goods_id', 'groups'],
                "properties": {
                    "total": {"type": "number"},
                    "goods_id": {"type": "string"},
                    'groups': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {}
                        }
                    }
                }
            }
        }
    }
