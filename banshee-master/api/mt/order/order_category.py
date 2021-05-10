from api.mt.mt import Mt
import os
import datetime
from random import randint

class Order_category(Mt):
    method = 'get'
    api = '/v1/order_category'
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
                    "List"
                ],
                "properties": {
                    "List": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "DisplayOrder": {
                                    "type": "number"
                                },
                                "DisplayName": {
                                    "type": "string"
                                },
                                "OrderStatus": {
                                    "type": "number"
                                },
                                "Quantity": {
                                    "type": "number"
                                },
                                "Hint": {
                                    "type": "string"
                                }
                            }
                        }
                    }
                }
            }
        }
    }