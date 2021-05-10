from api.mt.mt import Mt
import os
import datetime
from random import randint


class V2_Order(Mt):
    method = 'get'
    api = '/v2/order?order_status=$order_status&offset=&size=$size'
    data = {}

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

    # expected_schema = {
    #     "$schema": "http://json-schema.org/draft-06/schema#",
    #     "title": "expected_data",
    #     "type": "object",
    #     "required": [
    #         "code",
    #         "time",
    #         "data"
    #     ],
    #     "properties": {
    #         "code": {
    #             "type": "number"
    #         },
    #         "time": {
    #             "type": "number"
    #         },
    #         "data": {
    #             "type": "object",
    #             "required": [
    #                 "offset",
    #                 "order_items"
    #             ],
    #             "properties": {
    #                 "offset": {
    #                     "type": "string"
    #                 },
    #                 "order_items": {
    #                     "type": "array",
    #                     "items": {
    #                         "type": "object",
    #                         "properties": {
    #                             "goods_list": {
    #                                 "type": "array",
    #                                 "items": {
    #                                     "type": "object",
    #                                     "properties": {
    #                                         "goods_id": {
    #                                             "type": "number"
    #                                         },
    #                                         "goods_name": {
    #                                             "type": "string"
    #                                         },
    #                                         "goods_icon": {
    #                                             "type": "string"
    #                                         },
    #                                         "goods_sku_id": {
    #                                             "type": "number"
    #                                         },
    #                                         "goods_specs": {
    #                                             "type": "array",
    #                                             "items": {
    #                                                 "type": "object",
    #                                                 "properties": {
    #                                                     "spec_id": {
    #                                                         "type": "number"
    #                                                     },
    #                                                     "spec_key": {
    #                                                         "type": "string"
    #                                                     },
    #                                                     "spec_value": {
    #                                                         "type": "string"
    #                                                     }
    #                                                 }
    #                                             }
    #                                         },
    #                                         "goods_unit_price": {
    #                                             "type": "number"
    #                                         },
    #                                         "goods_quantity": {
    #                                             "type": "number"
    #                                         },
    #                                         "compensation_service": {
    #                                             "type": "array",
    #                                             "items": {
    #                                                 "type": "object",
    #                                                 "properties": {
    #                                                     "type": {
    #                                                         "type": "number"
    #                                                     },
    #                                                     "title": {
    #                                                         "type": "string"
    #                                                     },
    #                                                     "desc": {
    #                                                         "type": "string"
    #                                                     },
    #                                                     "btn": {
    #                                                         "type": "string"
    #                                                     },
    #                                                     "link": {
    #                                                         "type": "string"
    #                                                     }
    #                                                 }
    #                                             }
    #                                         }
    #                                     }
    #                                 }
    #                             },
    #                             "goods_count": {
    #                                 "type": "number"
    #                             },
    #                             "order_type": {
    #                                 "type": "number"
    #                             },
    #                             "coupon_desc": {
    #                                 "type": "string"
    #                             },
    #                             "process_status": {
    #                                 "type": "number"
    #                             },
    #                             "finished_status": {
    #                                 "type": "number"
    #                             },
    #                             "refund_status": {
    #                                 "type": "number"
    #                             },
    #                             "lock_status": {
    #                                 "type": "number"
    #                             },
    #                             "cancelable": {
    #                                 "type": "number"
    #                             },
    #                             "can_urge_ship": {
    #                                 "type": "number"
    #                             },
    #                             "sign_reward_coins": {
    #                                 "type": "number"
    #                             },
    #                             "recv_type": {
    #                                 "type": "number"
    #                             },
    #                             "can_delay_sign": {
    #                                 "type": "number"
    #                             },
    #                             "can_add_review": {
    #                                 "type": "number"
    #                             },
    #                             "review_reward_coins": {
    #                                 "type": "number"
    #                             },
    #                             "payment_deadline": {
    #                                 "type": "number"
    #                             },
    #                             "payment_money_type": {
    #                                 "type": "number"
    #                             },
    #                             "payment_total": {
    #                                 "type": "number"
    #                             },
    #                             "payment_express": {
    #                                 "type": "number"
    #                             },
    #                             "payment_system_discount": {
    #                                 "type": "number"
    #                             },
    #                             "payment_mall_discount": {
    #                                 "type": "number"
    #                             },
    #                             "money_saved": {
    #                                 "type": "string"
    #                             },
    #                             "payment_method": {
    #                                 "type": "number"
    #                             },
    #                             "payment_status": {
    #                                 "type": "number"
    #                             },
    #                             "payment_time": {
    #                                 "type": "number"
    #                             },
    #                             "buyer_confirm_delay_count": {
    #                                 "type": "number"
    #                             },
    #                             "group_order_id": {
    #                                 "type": "string"
    #                             },
    #                             "logistic_id": {
    #                                 "type": "number"
    #                             },
    #                             "refund_id": {
    #                                 "type": "string"
    #                             },
    #                             "refundable_amount": {
    #                                 "type": "number"
    #                             },
    #                             "id": {
    #                                 "type": "string"
    #                             },
    #                             "mall_id": {
    #                                 "type": "number"
    #                             },
    #                             "mall_name": {
    #                                 "type": "string"
    #                             },
    #                             "mall_icon": {
    #                                 "type": "string"
    #                             },
    #                             "status_text": {
    #                                 "type": "string"
    #                             },
    #                             "auto_sign": {
    #                                 "type": "boolean"
    #                             },
    #                             "forbid_refund": {
    #                                 "type": "boolean"
    #                             },
    #                             "create_at": {
    #                                 "type": "number"
    #                             },
    #                             "express_take_goods": {
    #                                 "type": "boolean"
    #                             },
    #                             "remind_text": {
    #                                 "type": "string"
    #                             },
    #                             "order_mall_name": {
    #                                 "type": "string"
    #                             },
    #                             "order_mall_icon": {
    #                                 "type": "string"
    #                             },
    #                             "order_mall_link": {
    #                                 "type": "string"
    #                             },
    #                             "buy_again_link": {
    #                                 "type": "string"
    #                             },
    #                             "is_evaluate": {
    #                                 "type": "boolean"
    #                             },
    #                             "evaluate_link": {
    #                                 "type": "string"
    #                             },
    #                             "order_review_link": {
    #                                 "type": "string"
    #                             },
    #                             "buy_prime_price": {
    #                                 "type": "number"
    #                             }
    #                         }
    #                     }
    #                 }
    #             }
    #         }
    #     }
    # }