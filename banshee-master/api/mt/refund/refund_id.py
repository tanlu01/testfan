from api.mt.mt import Mt
import os
import datetime
from random import randint

class Refund_id(Mt):
    method = 'get'
    api = '/v1/refund/$refund_id'
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
                    "status",
                    "detail",
                    "address"
                ],
                "properties": {
                    "status": {
                        "type": "number"
                    },
                    "detail": {
                        "type": "object",
                        "required": [
                            "id",
                            "type",
                            "speed_refund",
                            "status",
                            "deadline",
                            "count_down_seconds",
                            "handler_id",
                            "amount",
                            "desc",
                            "money_type",
                            "received",
                            "reason_type",
                            "operator_tel",
                            "create_at",
                            "return_method",
                            "return_account",
                            "return_status",
                            "return_trace",
                            "steps",
                            "logistic_id",
                            "express_name",
                            "tracking_num",
                            "buyer_avatar",
                            "buyer_name",
                            "mall_id",
                            "mall_name",
                            "mall_icon",
                            "goods_id",
                            "goods_name",
                            "goods_icon",
                            "order_id",
                            "recv_type",
                            "order_status",
                            "order_refund_status",
                            "order_lock_status",
                            "order_payment_total",
                            "need_express_fee",
                            "aftersale_reason_id",
                            "aftersale_reason_name",
                            "aftersale_tag_ids",
                            "aftersale_tag_names",
                            "free_refund_exp_status",
                            "free_refund_amount",
                            "service_tag",
                            "refund_express_amount",
                            "express_payer",
                            "refund_express_pay_lists",
                            "service_type"
                        ],
                        "properties": {
                            "id": {
                                "type": "string"
                            },
                            "type": {
                                "type": "number"
                            },
                            "speed_refund": {
                                "type": "number"
                            },
                            "status": {
                                "type": "number"
                            },
                            "deadline": {
                                "type": "number"
                            },
                            "count_down_seconds": {
                                "type": "number"
                            },
                            "handler_id": {
                                "type": "number"
                            },
                            "amount": {
                                "type": "number"
                            },
                            "desc": {
                                "type": "string"
                            },
                            "money_type": {
                                "type": "number"
                            },
                            "received": {
                                "type": "number"
                            },
                            "reason_type": {
                                "type": "number"
                            },
                            "operator_tel": {
                                "type": "string"
                            },
                            "create_at": {
                                "type": "number"
                            },
                            "return_method": {
                                "type": "number"
                            },
                            "return_account": {
                                "type": "string"
                            },
                            "return_status": {
                                "type": "number"
                            },
                            "return_trace": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {}
                                }
                            },
                            "steps": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "operator_role": {
                                            "type": "number"
                                        },
                                        "operator_avatar": {
                                            "type": "string"
                                        },
                                        "operation_desc": {
                                            "type": "string"
                                        },
                                        "operation_type": {
                                            "type": "number"
                                        },
                                        "remark_text": {
                                            "type": "string"
                                        },
                                        "remark_imgs": {
                                            "type": "array",
                                            "items": [
                                                {
                                                    "type": "string"
                                                }
                                            ]
                                        },
                                        "create_at": {
                                            "type": "number"
                                        }
                                    }
                                }
                            },
                            "logistic_id": {
                                "type": "number"
                            },
                            "express_name": {
                                "type": "string"
                            },
                            "tracking_num": {
                                "type": "string"
                            },
                            "buyer_avatar": {
                                "type": "string"
                            },
                            "buyer_name": {
                                "type": "string"
                            },
                            "mall_id": {
                                "type": "number"
                            },
                            "mall_name": {
                                "type": "string"
                            },
                            "mall_icon": {
                                "type": "string"
                            },
                            "goods_id": {
                                "type": "number"
                            },
                            "goods_name": {
                                "type": "string"
                            },
                            "goods_icon": {
                                "type": "string"
                            },
                            "order_id": {
                                "type": "string"
                            },
                            "recv_type": {
                                "type": "number"
                            },
                            "order_status": {
                                "type": "number"
                            },
                            "order_refund_status": {
                                "type": "number"
                            },
                            "order_lock_status": {
                                "type": "number"
                            },
                            "order_payment_total": {
                                "type": "number"
                            },
                            "need_express_fee": {
                                "type": "boolean"
                            },
                            "aftersale_reason_id": {
                                "type": "number"
                            },
                            "aftersale_reason_name": {
                                "type": "string"
                            },
                            "aftersale_tag_names": {
                                "type": "string"
                            },
                            "free_refund_exp_status": {
                                "type": "number"
                            },
                            "free_refund_amount": {
                                "type": "number"
                            },
                            "service_tag": {
                                "type": "string"
                            },
                            "refund_express_amount": {
                                "type": "number"
                            },
                            "express_payer": {
                                "type": "number"
                            },
                            "refund_express_pay_lists": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "pay_method": {
                                            "type": "number"
                                        },
                                        "pay_method_name": {
                                            "type": "string"
                                        }
                                    }
                                }
                            },
                            "service_type": {
                                "type": "number"
                            }
                        }
                    },
                    "address": {
                        "type": "object",
                        "required": [
                            "id",
                            "receiver_name",
                            "receiver_tel",
                            "province_id",
                            "province",
                            "city_id",
                            "city",
                            "district_id",
                            "district",
                            "address_detail",
                            "tag"
                        ],
                        "properties": {
                            "id": {
                                "type": "number"
                            },
                            "receiver_name": {
                                "type": "string"
                            },
                            "receiver_tel": {
                                "type": "string"
                            },
                            "province_id": {
                                "type": "number"
                            },
                            "province": {
                                "type": "string"
                            },
                            "city_id": {
                                "type": "number"
                            },
                            "city": {
                                "type": "string"
                            },
                            "district_id": {
                                "type": "number"
                            },
                            "district": {
                                "type": "string"
                            },
                            "address_detail": {
                                "type": "string"
                            },
                            "tag": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
        }
    }
