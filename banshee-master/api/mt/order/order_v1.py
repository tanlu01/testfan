from api.mt.mt import Mt


class OrderV1(Mt):
    method = 'post'
    api = '/v1/order'
    data = {
        "address_id": 391395,
        "goods_group_id": 0,
        "goods_id": 102858,
        "goods_quantity": 1,
        "goods_sku_id": 99937,
        "group_order_id": "",
        "payment_method": 3,
        "payment_money_type": 0,
        "coupon_id": [],
        "selected_cash_card": [],
        "use_coins": False,
        "remark": "",
        "selected_mall_coupon_id": "",
        "selected_system_coupon_id": "",
        "system_promotion_id": "",
        "expected_payment_total": 1,
        "selected_buy_prime": False
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

    expected_schema1 = {
        "$schema": "http://json-schema.org/draft-06/schema",
        "type": "object",
        "title": "The root schema",
        "required": [
            "code",
            "data",
            "time"
        ],
        "properties": {
            "code": {
                "type": "integer",
                "title": "The code schema"
            },
            "data": {
                "type": "object",
                "title": "The data schema",
                "required": [
                    "fail_msg",
                    "no_change_address",
                    "order_id",
                    "order_status",
                    "payment_deadline",
                    "seckill_sold_out_coupon"
                ],
                "properties": {
                    "fail_msg": {
                        "type": "string",
                        "title": "The fail_msg schema"
                    },
                    "no_change_address": {
                        "type": "boolean",
                        "title": "The no_change_address schema"
                    },
                    "order_id": {
                        "type": "string",
                        "title": "The order_id schema"
                    },
                    "order_status": {
                        "type": "integer",
                        "title": "The order_status schema"
                    },
                    "payment_deadline": {
                        "type": "integer",
                        "title": "The payment_deadline schema"
                    },
                    "seckill_sold_out_coupon": {
                        "type": "null",
                        "title": "The seckill_sold_out_coupon schema"
                    }
                }
            },
            "time": {
                "type": "integer",
                "title": "The time schema"
            }
        }
    }
