from api.mt.mt import Mt
import os
import datetime
from random import randint


class Order(Mt):
    method = 'get'
    api = '/v1/search/order?q=$search_keyword&offset=&size=10'
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
                    "offset",
                    "order_items"
                ],
                "properties": {
                    "offset": {
                        "type": "string"
                    },
                    "order_items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {

                            }
                        }
                    }
                }
            }
        }
    }
