from api.mt.mt import Mt
import os
import datetime
from random import randint

class Tips(Mt):
    method = 'get'
    api = '/v1/order_check/tips?goods_id=$goods_id&sku_id=$sku_id'
    data = {}


    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

    expected_schema = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "title": "expected_data",
        "type": "object",
        "required": [
            "code",
            "time",
            "data"
        ],
        "properties": {
            "code": {
                "type": "number"
            },
            "time": {
                "type": "number"
            },
            "data": {
                "type": "object",
                "required": [
                    "text",
                    "position",
                    "bg_img",
                    "bg_img_ratio"
                ],
                "properties": {
                    "text": {
                        "type": "string"
                    },
                    "position": {
                        "type": "number"
                    },
                    "bg_img": {
                        "type": "string"
                    },
                    "bg_img_ratio": {
                        "type": "string"
                    }
                }
            }
        }
    }
