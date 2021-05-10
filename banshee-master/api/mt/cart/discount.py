from api.mt.mt import Mt
import os
import datetime
from random import randint


class Discount_v2(Mt):
    method = 'post'
    api = '/v2/cart/discount'
    data = {
        "no_promotion": False,
        "skus": [{
            "goods_id": "107893",
            "mall_id": 100005,
            "promotion_id": "",
            "quantity": 1,
            "sku_id": 101749,
            "sku_price": 777777777
        }],
        "system_promotion_id": ""
    }

    expected_schema = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "title": "expected_data",
        "type": "object",
        "required": ["code", "time", 'data'],
        "properties": {
            "code": {"type": "number"},
            "time": {"type": "number"},
            "data": {
                "type": "object",
                "required": ["total_price", 'payment_price', 'total_discount', 'plt_discount',
                             'mall_discount', 'invalid_skus', 'coupons', 'tips', 'promotions',
                             'promotion_hint', 'discount_detail', 'system_promotion_id'],
                "properties": {
                    "total_price": {"type": "number"},
                    "payment_price": {"type": "number"},
                    "total_discount": {"type": "number"},
                    "plt_discount": {"type": "number"},
                    "mall_discount": {"type": "number"},
                    "invalid_skus": {"type": None},
                    "coupons": {"type": None},
                    "tips": {"type": 'string'},
                    "promotions": {
                        "type": 'array',
                        'items': 'object',
                        'properties': {}
                    },
                    "promotion_hint": {"type": 'string'},
                    "discount_detail": {
                        "type": 'array',
                        'items': 'object',
                        'properties': {}
                    },
                    "system_promotion_id": {"type": 'string'}
                }
            }
        }
    }


class Discount_v1(Mt):
    method = 'post'
    api = '/v1/cart/discount'
    data = {
        "no_promotion": False,
        "skus": [{
            "goods_id": "107893",
            "mall_id": 100005,
            "promotion_id": "",
            "quantity": 1,
            "sku_id": 101749,
            "sku_price": 777777777
        }],
        "system_promotion_id": ""
    }
