from api.mms.mms_ import Mms


class UpDownGoods(Mms):
    method = 'post'
    api = '/api/goods/upDownGoods'
    data = {
        'goods_id': "",
        'is_onsale': 10
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
    #             "required": ["activities"],
    #             "properties": {
    #                 "activities": {
    #                     "type": "array",
    #                     'items': {
    #                         'type': 'object',
    #                         'properties': {
    #                             "act_cate": {"type": "number"},
    #                             "audit_status": {"type": "string"},
    #                             "calculate_type": {"type": "number"},
    #                             "goods_id": {"type": "string"},
    #                             "id": {"type": "string"},
    #                             "name": {"type": "string"},
    #                             "sub_type": {"type": "string"},
    #                             "type": {"type": "string"},
    #                             "type_text": {"type": "string"}
    #                         }
    #                     }
    #                 },
    #             }
    #         }
    #     }
    # }