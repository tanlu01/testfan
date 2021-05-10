from api.mt.mt import Mt


class Coupons(Mt):
    method = 'get'
    api = '/v2/mall/$mall_id/coupons'
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
                                "name": {
                                    "type": "string"
                                },
                                "sub_name": {
                                    "type": "string"
                                },
                                "mall_id": {
                                    "type": "number"
                                },
                                "discount": {
                                    "type": "object",
                                    "required": [
                                        "type",
                                        "value",
                                        "value_uint"
                                    ],
                                    "properties": {
                                        "type": {
                                            "type": "number"
                                        },
                                        "value": {
                                            "type": "string"
                                        },
                                        "value_uint": {
                                            "type": "number"
                                        }
                                    }
                                },
                                "usetime": {
                                    "type": "object",
                                    "required": [
                                        "begin",
                                        "end"
                                    ],
                                    "properties": {
                                        "begin": {
                                            "type": "number"
                                        },
                                        "end": {
                                            "type": "number"
                                        }
                                    }
                                },
                                "has_received": {
                                    "type": "boolean"
                                },
                                "has_useable": {
                                    "type": "boolean"
                                },
                                "should_prime": {
                                    "type": "number"
                                },
                                "btn_status": {
                                    "type": "number"
                                },
                                "type": {
                                    "type": "number"
                                }
                            }
                        }
                    }
                }
            }
        }
    }


class DetailLegoProject(Mt):
    method = 'get'
    api = '/v2/lego/page'
    data = {
        'project_id': "",
        'render': None,
        'open_filter': None
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }


class ReceiveCoupon(Mt):
    method = 'post'
    api = '/v2/user_coupon'
    data = {
        'coupon_id': "8612742583998791680"
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
