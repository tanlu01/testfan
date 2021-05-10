from api.mt.mt import Mt


class Coupons(Mt):
    method = 'get'
    api = '/v1/mall/$mall_id/coupons'
    data = {}

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
                    "coupons"
                ],
                "properties": {
                    "coupons": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "mall_id": {
                                    "type": "number"
                                },
                                "mall_name": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                },
                                "sub_name": {
                                    "type": "string"
                                },
                                "amount": {
                                    "type": "number"
                                },
                                "type": {
                                    "type": "number"
                                },
                                "status": {
                                    "type": "number"
                                },
                                "begin": {
                                    "type": "number"
                                },
                                "end": {
                                    "type": "number"
                                },
                                "order_id": {
                                    "type": "string"
                                },
                                "user_coupon_id": {
                                    "type": "number"
                                },
                                "can_taken_count": {
                                    "type": "number"
                                },
                                "is_taken_out": {
                                    "type": "boolean"
                                },
                                "remain": {
                                    "type": "number"
                                },
                                "received_time": {
                                    "type": "number"
                                },
                                "goods_id": {
                                    "type": "string"
                                },
                                "min_price": {
                                    "type": "number"
                                }
                            }
                        }
                    }
                }
            }
        }
    }

