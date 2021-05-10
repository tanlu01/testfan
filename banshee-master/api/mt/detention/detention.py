from api.mt.mt import Mt
import os
import datetime
from random import randint


class During_pay(Mt):
    method = 'post'
    api = '/v1/detention/during_pay'
    data = {
        "goods_info": {
            "goods_id": 1104,
            "sku_id": 1023
        },
        "order_id": "1612591533165428931"
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }


class Order_cancel(Mt):
    method = 'post'
    api = '/v1/detention/order_cancel'
    data = {
        "goods_info": {
            "goods_id": 110436,
            "sku_id": 102311
        },
        "order_id": "1612591533165428931"
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
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
                "required": ["alert_view"],
                "properties": {
                    "alert_view": {
                        "type": "object",
                        'required': ['mark_value', 'mark_value_type', 'title', 'text', 'mark', 'buttons',
                                     'extra', 'image', 'image_ratio', 'image_link', 'alert_type', 'show_time',
                                     'deadline', 'target_url', 'popup', 'tdata'],
                        'properties': {
                            'mark_value': {'type': 'string'},
                            'mark_value_type': {'type': 'number'},
                            'title': {'type': 'string'},
                            'text': {'type': 'string'},
                            'mark': {'type': 'string'},
                            'buttons': {'type': None},
                            'extra': {'type': None},
                            'image': {'type': 'string'},
                            'image_ratio': {'type': 'string'},
                            'image_link': {'type': 'string'},
                            'alert_type': {'type': 'number'},
                            'show_time': {'type': 'number'},
                            'deadline': {'type': 'number'},
                            'target_url': {'type': 'string'},
                            'tdata': {'type': 'string'},
                            'popup': {
                                'type': 'object',
                                'required': ['bg_img', 'title', 'popup_type', 'amount', 'left_button', 'middle_button',
                                             'right_button'],
                                'properties': {
                                    'bg_img': {'type': 'string'},
                                    'title': {'type': 'string'},
                                    'popup_type': {'type': 'string'},
                                    'amount': {'type': 'number'},
                                    'left_button': {'type': None},
                                    'middle_button': {'type': None},
                                    'right_button': {'type': None}
                                }
                            }
                        }
                    }
                }
            }
        }
    }
