from api.mt.mt import Mt


class PaymentChannelStatus(Mt):
    method = 'post'
    api = '/payment_channel_status'
    data = {
        "platform": 30,
        "goods_id": 110436,
        "goods_list": [],
        "page": "order_checkout"
    }

    success_resp = {'code': 0}
    payment_method = {
        0: '微信支付',
        3: '支付宝',
        9: '花呗'
    }

    expected_schema = {
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
                    "default_method",
                    "folding_methods",
                    "payment_methods"
                ],
                "properties": {
                    "default_method": {
                        "type": "integer",
                        "title": "The default_method schema"
                    },
                    "folding_methods": {
                        "type": "array",
                        "title": "The folding_methods schema",
                        "items": {
                            "anyOf": [
                                {
                                    "type": "object",
                                    "title": "The first anyOf schema",
                                    "required": [
                                        "act_text",
                                        "desc",
                                        "payment_method",
                                        "title"
                                    ],
                                    "properties": {
                                        "act_text": {
                                            "type": "string",
                                            "title": "The act_text schema"
                                        },
                                        "desc": {
                                            "type": "string",
                                            "title": "The desc schema"
                                        },
                                        "payment_method": {
                                            "type": "integer",
                                            "title": "The payment_method schema"
                                        },
                                        "title": {
                                            "type": "string",
                                            "title": "The title schema"
                                        }
                                    }
                                }
                            ]
                        }
                    },
                    "payment_methods": {
                        "type": "array",
                        "title": "The payment_methods schema",
                        "items": {
                            "anyOf": [
                                {
                                    "type": "object",
                                    "title": "The first anyOf schema",
                                    "required": [
                                        "act_text",
                                        "desc",
                                        "payment_method",
                                        "title"
                                    ],
                                    "properties": {
                                        "act_text": {
                                            "type": "string",
                                            "title": "The act_text schema"
                                        },
                                        "desc": {
                                            "type": "string",
                                            "title": "The desc schema"
                                        },
                                        "payment_method": {
                                            "type": "integer",
                                            "title": "The payment_method schema"
                                        },
                                        "title": {
                                            "type": "string",
                                            "title": "The title schema"
                                        }
                                    }
                                }
                            ]
                        }
                    }
                }
            },
            "time": {
                "type": "integer",
                "title": "The time schema"
            }
        }
    }
