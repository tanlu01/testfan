from api.mt.mt import Mt
import os
import datetime
from random import randint


class Goods_list_Id(Mt):
    method = 'get'
    api = '/v1/favorite/goods/list/id'
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
                "required": ["ids"],
                "properties": {
                    "ids": {
                        "type": "array",
                        'items': {
                            'type': 'object',
                            'properties': {}
                        }
                    }
                }
            }
        }
    }
