from api.mt.mt import Mt
import os
import datetime
from random import randint


class Order(Mt):
    method = 'post'
    api = '/v1/recharge/order'
    data = {
        "address_id": 0,
        "coupon_id": [
            "string"
        ],
        "expected_payment_total": 0,
        "expected_unit_price": 0,
        "goods_group_id": 0,
        "goods_id": 0,
        "goods_quantity": 0,
        "goods_sku_id": 0,
        "group_order_id": "string",
        "last_address_code": 0,
        "mall_promotion_id": "string",
        "order_check_attach": "string",
        "out_source": {
            "__docs": "string",
            "activity_id": 0,
            "ref_key_param": "string",
            "ref_page_id": "string",
            "ref_page_name": "string",
            "source_ref_key_param": "string",
            "source_ref_page_id": "string",
            "source_ref_page_name": "string",
            "source_ref_pos_id": "string"
        },
        "payment_method": 0,
        "payment_money_type": 0,
        "real_name_id": 0,
        "recv_mobile": "string",
        "remark": "string",
        "selected_buy_prime": True,
        "selected_cash_card": [
            "string"
        ],
        "selected_mall_coupon_id": "string",
        "selected_system_coupon_id": "string",
        "share_code": "string",
        "system_promotion_id": "string",
        "tb_nickname": "string",
        "tb_open_id": "string",
        "use_coins": True
    }  
    # 参数添加无信息

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
