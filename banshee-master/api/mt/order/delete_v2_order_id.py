from api.mt.mt import Mt
import os
import datetime
from random import randint


class Delete_V2_Order_id(Mt):
    method = 'delete'
    api = '/v2/order/$order_id'
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
                    "order_id",
                    "status"
                ],
                "properties": {
                    "order_id": {
                        "type": "string"
                    },
                    "status": {
                        "type": "number"
                    }
                }
            }
        }
    }