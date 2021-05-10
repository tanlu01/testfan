from api.mt.mt import Mt
import os
import datetime
from random import randint


class ShoppingCart(Mt):
    method = 'get'
    api = '/v1/cart?offset=&size=$size_id'
    data = {

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
    #             "required": ["items", 'length', 'offset'],
    #             "properties": {
    #                 "length": {"type": "number"},
    #                 "offset": {"type": "string"},
    #                 'items': {
    #                     'type': 'array',
    #                     'items': {
    #                         'type': 'object',
    #                         'properties': {
    #                             'mall_id': {'type': 'number'},
    #                             'mall_name': {'type': 'string'},
    #                             'mall_logo': {'type': 'string'},
    #                             'coupons': {
    #                                 'type': 'array',
    #                                 'items': {
    #                                     'type': 'object',
    #                                     'properties': {
    #                                         'id': {'type': 'string'},
    #                                         'name': {'type': 'string'},
    #                                         'sub_name': {'type': 'string'},
    #                                         'mall_id': {'type': 'number'},
    #                                         'discount': {
    #                                             'type': 'object',
    #                                             "required": ["type", 'value', 'value_uint'],
    #                                             'properties': {
    #                                                 'type': {'type': 'number'},
    #                                                 'value': {'type': 'string'},
    #                                                 'value_uint': {'type': 'number'}
    #                                             }
    #                                         },
    #                                         'usetime': {
    #                                                 'type': 'object',
    #                                                 "required": ["begin", 'end'],
    #                                                 'properties': {
    #                                                     'begin': {'type': 'number'},
    #                                                     'end': {'type': 'number'}
    #                                             }
    #                                         },
    #                                         'has_received': {'type': 'boolean'},
    #                                         'has_useable': {'type': 'boolean'},
    #                                         'should_prime': {'type': 'number'},
    #                                         'btn_status': {'type': 'number'},
    #                                         'type': {'type': 'number'}
    #                                     }
    #                                 }
    #                             },
    #                             'goods': {
    #                                 'type': 'array',
    #                                 'items': {
    #                                     'type': 'object',
    #                                     'properties': {
    #                                         'goods_id': {'type': 'string'},
    #                                         'goods_name': {'type': 'string'},
    #                                         'short_name': {'type': 'string'},
    #                                         'thumb_url': {'type': 'string'},
    #                                         'ethumb': {
    #                                             'type': 'object',
    #                                             "required": ["img", 'ratio'],
    #                                             'properties': {
    #                                                 'img': {'type': 'string'},
    #                                                 'ratio': {'type': 'string'}
    #                                             }
    #                                         },
    #                                         'market_price': {'type': 'number'},
    #                                         'min_group_price': {'type': 'number'},
    #                                         'min_normal_price': {'type': 'number'},
    #                                         'min_price': {'type': 'number'},
    #                                         'sales': {'type': 'number'},
    #                                         'sales_text': {'type': 'string'},
    #                                         'sales_whole_text': {'type': 'string'},
    #                                         'mall_id': {'type': 'number'},
    #                                         'footnote': {'type': 'string'},
    #                                         'promotion_mark': {'type': 'string'},
    #                                         'import_mark': {'type': 'string'},
    #                                         'marks_front': {'type': None},
    #                                         'marks_back': {
    #                                             'type': 'array',
    #                                             'items': {
    #                                                 'type': 'object',
    #                                                 'properties': {
    #                                                     'id': {'type': 'string'},
    #                                                     'text': {'type': 'string'},
    #                                                     'style': {'type': 'number'},
    #                                                     'name': {'type': 'string'},
    #                                                     'img_url': {'type': 'string'},
    #                                                     'img_ratio': {'type': 'string'},
    #                                                     'link': {'type': 'string'},
    #                                                     'icon_url': {'type': 'string'},
    #                                                     'icon_ratio': {'type': 'string'}
    #                                                 }
    #                                             }
    #                                         },
    #                                         'marks_rear': {'type': None},
    #                                         'mall': {
    #                                             'type': 'object',
    #                                             "required": ["mall_id", "mall_name", 'location', 'labels'],
    #                                             'properties': {
    #                                                 'mall_id': {'type': 'string'},
    #                                                 'mall_name': {'type': 'string'},
    #                                                 'location': {'type': 'string'},
    #                                                 'labels': {'type': None}
    #                                             }
    #                                         },
    #                                         'service_promise_mark': {'type': None},
    #                                         'show_price': {'type': 'number'},
    #                                         'sku_id': {'type': 'number'},
    #                                         'sku_thumb_url': {'type': 'string'},
    #                                         'stock': {'type': 'number'},
    #                                         'quantity': {'type': 'number'},
    #                                         'sku_desc': {'type': 'string'},
    #                                         'sku_spec_key': {'type': 'string'},
    #                                         'status': {'type': 'number'},
    #                                         'sku_price': {'type': 'number'},
    #                                         'sku_prime_price': {'type': 'number'},
    #                                         'goods_buy_limit': {'type': 'number'},
    #                                         'promotions': {
    #                                             'type': 'array',
    #                                             'items': {
    #                                                 'type': 'object',
    #                                                 'properties': {}
    #                                             }
    #                                         }
    #                                     }
    #                                 }
    #                             },
    #                             'mall_link': {'type': 'string'}
    #                         }
    #                     }
    #                 }
    #             }
    #         }
    #     }
    # }
