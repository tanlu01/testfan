from api.mt.mt import Mt


class AliMarketingConsult(Mt):
    method = 'post'
    api = '/ali_marketing_consult'
    data = {
        "mobile": "15021721254",
        "biz_scene": "ORDER_PAGE",
        "order_payment_total": 9899
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

    expected_schema = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "title": "expected_data",
        "type": "object",
        "required": [
            "code",
            "time",
            "data"
        ],
        "properties": {
            "code": {
                "type": "number"
            },
            "time": {
                "type": "number"
            },
            "data": {
                "type": "object",
                "required": [
                    "text"
                ],
                "properties": {
                    "text": {
                        "type": "string"
                    }
                }
            }
        }
    }
