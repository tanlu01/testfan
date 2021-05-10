from api.mms.mms_ import Mms


class GoodsList(Mms):
    method = 'get'
    api = '/api/goods/list'
    data = {
        'start': 0,
        'count': 500,
        'status': 1
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

    # expected_schema = {
    #     "$schema": "http://json-schema.org/draft-06/schema#",
    #     "title": "expected_data",
    #     "type": "object",
    #     "required": ["code", "payload"],
    #     "properties": {
    #         "code": {"type": "number"},
    #         "payload": {
    #             "type": "object",
    #             "required": ["count", "is_cost_mall", 'is_es', 'is_open', 'list'],
    #             "properties": {
    #                 'count': {"type": "number"},
    #                 'is_cost_mall': {"type": "boolean"},
    #                 'is_es': {"type": "boolean"},
    #                 'is_open': {"type": "string"},
    #                 "list": {
    #                     "type": "array",
    #                     'items': {
    #                         'type': 'object',
    #                         'properties': {
    #                             'cat_id': {"type": "string"},
    #                             'cat_id_1': {"type": "string"},
    #                             'cat_id_2': {"type": "string"},
    #                             'cost_range': {"type": "string"},
    #                             'desc_rate': {"type": "string"},
    #                             'goods_id': {"type": "string"},
    #                             'is_illegal': {"type": "string"},
    #                             'is_onsale': {"type": "string"},
    #                             'mall_rank': {"type": "string"},
    #                             'max_normal_price': {"type": "string"},
    #                             'max_prime_price': {"type": "string"},
    #                             'min_normal_price': {"type": "string"},
    #                             'min_prime_price': {"type": "string"},
    #                             'name': {"type": "string"},
    #                             'order_count': {"type": "number"},
    #                             'out_goods_sn': {"type": "string"},
    #                             'overall_score': {"type": "string"},
    #                             'quantity': {"type": "number"},
    #                             'sales': {"type": "number"},
    #                             'service_rate': {"type": "string"},
    #                             'ship_rate': {"type": "string"},
    #                             'thumb_url': {"type": "string"},
    #                             'video_id': {"type": "number"},
    #                         }
    #                     }
    #                 }
    #             }
    #         }
    #     }
    # }
