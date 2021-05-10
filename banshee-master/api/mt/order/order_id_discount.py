from api.mt.mt import Mt
import os
import datetime
from random import randint


class Discount(Mt):
    method = 'get'
    api = '/v1/order/$order_id/discount'
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
                    "coins_discount",
                    "total_coins",
                    "payment_total"
                ],
                "properties": {
                    "coins_discount": {
                        "type": "number"
                    },
                    "total_coins": {
                        "type": "number"
                    },
                    "payment_total": {
                        "type": "number"
                    }
                }
            }
        }
    }