from api.mt.mt import Mt


class OrderV2(Mt):
    method = 'post'
    api = '/v2/order'
    data = {
        "address_id": 0,
        "auto_select_system_coupon": True,
        "auto_select_cash_card": True,
        "selected_cash_card": [],
        "order_items": [
            {
                "auto_select_mall_coupon": False,
                "coupon_id": "0",
                "mall_id": 100078,
                "remark": "",
                "order_goods": [
                    {
                        "expected_unit_price": 1,
                        "goods_id": 102858,
                        "goods_quantity": 1,
                        "goods_sku_id": 99937
                    }
                ]
            }
        ],
        "payment_method": 3,
        "payment_money_type": 0,
        "pt_coupon_id": "0",
        "real_name_id": 0,
        "recv_mobile": "15755337793",
        "type": 1,
        "use_coins": False,
        "system_promotion_id": "",
        "last_selected_type": 0,
        "expected_payment_total": 1,
        "selected_buy_prime": False,
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
