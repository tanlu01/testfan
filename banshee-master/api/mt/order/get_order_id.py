from api.mt.mt import Mt
import os
import datetime
from random import randint


class Get_Order_id(Mt):
    method = 'get'
    api = '/v1/order/$order_id'
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
                    "id",
                    "mall_id",
                    "mall_name",
                    "mall_icon",
                    "order_mall_name",
                    "order_mall_icon",
                    "order_mall_link",
                    "buy_again_link",
                    "mall_tel",
                    "goods_link",
                    "goods_id",
                    "goods_name",
                    "goods_desc",
                    "goods_sku_id",
                    "goods_snap_id",
                    "goods_group_id",
                    "goods_quantity",
                    "goods_icon",
                    "goods_specs",
                    "goods_unit_price",
                    "create_at",
                    "lucky_draw_id",
                    "group_order_id",
                    "ship_deadline",
                    "remark",
                    "buyer_address",
                    "recv_mobile",
                    "mall_confirm_deadline",
                    "mall_confirm_time",
                    "buyer_confirm_deadline",
                    "buyer_confirm_time",
                    "buyer_confirm_delay_count",
                    "payment_deadline",
                    "payment_money_type",
                    "payment_total",
                    "payment_express",
                    "payment_system_discount",
                    "payment_activity_discount",
                    "payment_mall_discount",
                    "money_saved",
                    "payment_method",
                    "payment_status",
                    "payment_time",
                    "coupon_desc",
                    "status_text",
                    "sub_status_text",
                    "logistic_id",
                    "express_name",
                    "tracking_num",
                    "refund_id",
                    "latest_aftersale_status",
                    "credit_snap_id",
                    "process_status",
                    "finished_status",
                    "refund_status",
                    "lock_status",
                    "cancelable",
                    "refundable_amount",
                    "can_urge_ship",
                    "can_delay_sign",
                    "can_add_review",
                    "recv_type",
                    "auto_sign",
                    "forbid_refund",
                    "review_reward_coins",
                    "sign_reward_coins",
                    "should_modify_real_name",
                    "payment_order_id",
                    "no_change_address",
                    "after_sign_redirect_link",
                    "is_evaluate",
                    "evaluate_link",
                    "order_review_link",
                    "compensation_service",
                    "buy_prime_price",
                    "activity_id",
                    "only_refund",
                    "used_fund_subsidy",
                    "order_fund"
                ],
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
                    "mall_icon": {
                        "type": "string"
                    },
                    "order_mall_name": {
                        "type": "string"
                    },
                    "order_mall_icon": {
                        "type": "string"
                    },
                    "order_mall_link": {
                        "type": "string"
                    },
                    "buy_again_link": {
                        "type": "string"
                    },
                    "mall_tel": {
                        "type": "string"
                    },
                    "goods_link": {
                        "type": "string"
                    },
                    "goods_id": {
                        "type": "number"
                    },
                    "goods_name": {
                        "type": "string"
                    },
                    "goods_desc": {
                        "type": "string"
                    },
                    "goods_sku_id": {
                        "type": "number"
                    },
                    "goods_snap_id": {
                        "type": "string"
                    },
                    "goods_group_id": {
                        "type": "number"
                    },
                    "goods_quantity": {
                        "type": "number"
                    },
                    "goods_icon": {
                        "type": "string"
                    },
                    "goods_specs": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "spec_id": {
                                    "type": "number"
                                },
                                "spec_key": {
                                    "type": "string"
                                },
                                "spec_value": {
                                    "type": "string"
                                }
                            }
                        }
                    },
                    "goods_unit_price": {
                        "type": "number"
                    },
                    "create_at": {
                        "type": "number"
                    },
                    "lucky_draw_id": {
                        "type": "number"
                    },
                    "group_order_id": {
                        "type": "string"
                    },
                    "ship_deadline": {
                        "type": "number"
                    },
                    "remark": {
                        "type": "string"
                    },
                    "buyer_address": {
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
                    },
                    "recv_mobile": {
                        "type": "string"
                    },
                    "mall_confirm_deadline": {
                        "type": "number"
                    },
                    "mall_confirm_time": {
                        "type": "number"
                    },
                    "buyer_confirm_deadline": {
                        "type": "number"
                    },
                    "buyer_confirm_time": {
                        "type": "number"
                    },
                    "buyer_confirm_delay_count": {
                        "type": "number"
                    },
                    "payment_deadline": {
                        "type": "number"
                    },
                    "payment_money_type": {
                        "type": "number"
                    },
                    "payment_total": {
                        "type": "number"
                    },
                    "payment_express": {
                        "type": "number"
                    },
                    "payment_system_discount": {
                        "type": "number"
                    },
                    "payment_activity_discount": {
                        "type": "number"
                    },
                    "payment_mall_discount": {
                        "type": "number"
                    },
                    "money_saved": {
                        "type": "string"
                    },
                    "payment_method": {
                        "type": "number"
                    },
                    "payment_status": {
                        "type": "number"
                    },
                    "payment_time": {
                        "type": "number"
                    },
                    "coupon_desc": {
                        "type": "string"
                    },
                    "status_text": {
                        "type": "string"
                    },
                    "sub_status_text": {
                        "type": "string"
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
                    "refund_id": {
                        "type": "string"
                    },
                    "latest_aftersale_status": {
                        "type": "number"
                    },
                    "credit_snap_id": {
                        "type": "string"
                    },
                    "process_status": {
                        "type": "number"
                    },
                    "finished_status": {
                        "type": "number"
                    },
                    "refund_status": {
                        "type": "number"
                    },
                    "lock_status": {
                        "type": "number"
                    },
                    "cancelable": {
                        "type": "number"
                    },
                    "refundable_amount": {
                        "type": "number"
                    },
                    "can_urge_ship": {
                        "type": "number"
                    },
                    "can_delay_sign": {
                        "type": "number"
                    },
                    "can_add_review": {
                        "type": "number"
                    },
                    "recv_type": {
                        "type": "number"
                    },
                    "auto_sign": {
                        "type": "boolean"
                    },
                    "forbid_refund": {
                        "type": "boolean"
                    },
                    "review_reward_coins": {
                        "type": "number"
                    },
                    "sign_reward_coins": {
                        "type": "number"
                    },
                    "should_modify_real_name": {
                        "type": "boolean"
                    },
                    "payment_order_id": {
                        "type": "string"
                    },
                    "no_change_address": {
                        "type": "boolean"
                    },
                    "after_sign_redirect_link": {
                        "type": "string"
                    },
                    "is_evaluate": {
                        "type": "boolean"
                    },
                    "evaluate_link": {
                        "type": "string"
                    },
                    "order_review_link": {
                        "type": "string"
                    },
                    "compensation_service": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type": {
                                    "type": "number"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "desc": {
                                    "type": "string"
                                },
                                "btn": {
                                    "type": "string"
                                },
                                "link": {
                                    "type": "string"
                                }
                            }
                        }
                    },
                    "buy_prime_price": {
                        "type": "number"
                    },
                    "activity_id": {
                        "type": "number"
                    },
                    "only_refund": {
                        "type": "boolean"
                    },
                    "used_fund_subsidy": {
                        "type": "number"
                    },
                    "order_fund": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {}
                        }
                    }
                }
            }
        }
    }