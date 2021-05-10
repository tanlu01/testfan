from api.mt.mt import Mt
import os
import datetime
from random import randint


class Extra(Mt):
    method = 'get'
    api = '/v2/goods/$goods_id/extra?activity_id=$activity_id'
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
                "required": ["goods_id", "skus"],
                "properties": {
                    "skus": {
                        "type": "array",
                        'items': {}
                    },
                    "goods_id": {"type": "string"}
                }
            }
        }
    }
