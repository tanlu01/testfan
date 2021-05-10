from api.mt.mt import Mt
import os
import datetime
from random import randint


class Connect_share(Mt):
    method = 'post'
    api = '/v1/goods/$goods_id/connect_share'
    data = {
        "mopenid": "string"
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
                "required": [],
                "properties": {}
            }
        }
    }
