from api.mt.mt import Mt
import os
import datetime
from random import randint


class Delete_malls_like(Mt):
    method = 'delete'
    api = '/v1/favorite/malls/like/$mall_id'
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
