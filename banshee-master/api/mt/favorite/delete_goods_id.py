from api.mt.mt import Mt
import os
import datetime
from random import randint


class Delete_goods_id(Mt):
    method = 'delete'
    api = '/v1/favorite/goods/like/$goods_id'
    data = {}

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

    expected_schema = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "title": "expected_data",
        "type": "object",
        "required": ["code", "time"],
        "properties": {
            "code": {"type": "number"},
            "time": {"type": "number"}
        }
    }
