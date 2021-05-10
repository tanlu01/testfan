from api.mt.mt import Mt
import os
import datetime
from random import randint


class Delete_cart_sku(Mt):
    method = 'delete'
    api = '/v1/cart/sku'
    data = {
        "goods_sku_ids": [{
            "goods_id": "12008",
            "sku_id": 67596
        }],
        "sku_ids": [67596]
    }

    success_resp = {
        'code': 0
    }
    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
    # expected_schema = {
    #     "$schema": "http://json-schema.org/draft-06/schema#",
    #     "title": "expected_data",
    #     "type": "object",
    #     "required": ["code", "time", 'data'],
    #     "properties": {
    #         "code": {"type": "number"},
    #         "time": {"type": "number"},
    #         "data": {
    #             "type": "object",
    #             "required": ["delta"],
    #             "properties": {
    #                 "delta": {"type": "number"},
    #             }
    #         }
    #     }
    # }