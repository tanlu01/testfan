from api.mt.mt import Mt


class Qualification(Mt):
    method = 'post'
    api = '/v1/mall/$mall_id/qualification'
    data = {
        "captcha_code": "string",
        "captcha_token": "string",
        "license_type": "qualification"
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
