from api.mt.mt import Mt


class OrderCheckV1(Mt):
    method = 'post'
    api = '/v1/order_check'
    data = {
        "__check_id": 1,
        "address_id": 398124,
        "expected_unit_price": 0,
        "payment_money_type": 0,
        "goods_group_id": 0,
        "goods_id": 110436,
        "goods_quantity": 1,
        "goods_sku_id": 102311,
        "group_order_id": "",
        "payment_method": 3,
        "auto_select_mall_coupon": True,
        "auto_select_system_coupon": True,
        "auto_select_cash_card": True,
        "coupon_id": [],
        "selected_system_coupon_id": "",
        "selected_mall_coupon_id": "",
        "system_promotion_id": "",
        "no_select_system_promotion": False,
        "selected_buy_prime": False,
        "auto_select_coins": False,
        "use_coins": True,
        "selected_cash_card": []
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
