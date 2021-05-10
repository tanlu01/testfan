from api.mt.mt import Mt
import os
import datetime
from random import randint


class V2_Paystatus(Mt):
    method = 'get'
    api = '/v2/order/union_order/$order_id/paystatus'
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
                    "pay_status"
                ],
                "properties": {
                    "order_id": {
                        "type": "string"
                    },
                    "pay_status": {
                        "type": "number"
                    }
                }
            }
        }
    }
