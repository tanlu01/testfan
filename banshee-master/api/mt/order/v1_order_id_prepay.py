from api.mt.mt import Mt


class V1Prepay(Mt):
    method = 'post'
    api = '/v1/order/$order_id/prepay'
    data = {
        "platform": 50,  # android app
        "payment_method": 3  # 支付方式0-9,11,12,18.18
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

    payment_method_dict = {
        0: 'weixin_json',
        9: 'alipay_json',
        3: 'alipay_json'
    }

    platform_dict = {
        50: 'android app'
    }
