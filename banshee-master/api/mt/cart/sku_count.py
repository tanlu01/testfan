from api.mt.mt import Mt
import os
import datetime
from random import randint


class Sku_count(Mt):
    method = 'post'
    api = '/v1/cart/sku_count'
    data = {
        "sku_count": [{
            "goods_id": "37645227",
            "quantity": 1,
            "sku_id": 115035
        }]
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


