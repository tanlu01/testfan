from api.mt.mt import Mt
import os
import datetime
from random import randint


class OrderDetail(Mt):
    method = 'get'
    api = '/v1/order/$order_id'
    data = {}

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
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
                    "activity_id",
                    "after_sign_redirect_link",
                    "auto_sign",
                    "buy_again_link",
                    "buy_prime_price",
                    "buyer_address",
                    "buyer_confirm_deadline",
                    "buyer_confirm_delay_count",
                    "buyer_confirm_time",
                    "can_add_review",
                    "can_delay_sign",
                    "can_urge_ship",
                    "cancelable",
                    "compensation_service",
                    "coupon_desc",
                    "create_at",
                    "credit_snap_id",
                    "evaluate_link",
                    "express_name",
                    "finished_status",
                    "forbid_refund",
                    "goods_desc",
                    "goods_group_id",
                    "goods_icon",
                    "goods_id",
                    "goods_link",
                    "goods_name",
                    "goods_quantity",
                    "goods_sku_id",
                    "goods_snap_id",
                    "goods_specs",
                    "goods_unit_price",
                    "group_order_id",
                    "id",
                    "is_evaluate",
                    "latest_aftersale_status",
                    "lock_status",
                    "logistic_id",
                    "lucky_draw_id",
                    "mall_confirm_deadline",
                    "mall_confirm_time",
                    "mall_icon",
                    "mall_id",
                    "mall_name",
                    "mall_tel",
                    "money_saved",
                    "no_change_address",
                    "only_refund",
                    "order_fund",
                    "order_mall_icon",
                    "order_mall_link",
                    "order_mall_name",
                    "order_review_link",
                    "payment_activity_discount",
                    "payment_deadline",
                    "payment_express",
                    "payment_mall_discount",
                    "payment_method",
                    "payment_money_type",
                    "payment_order_id",
                    "payment_status",
                    "payment_system_discount",
                    "payment_time",
                    "payment_total",
                    "process_status",
                    "recv_mobile",
                    "recv_type",
                    "refund_id",
                    "refund_status",
                    "refundable_amount",
                    "remark",
                    "review_reward_coins",
                    "ship_deadline",
                    "should_modify_real_name",
                    "sign_reward_coins",
                    "status_text",
                    "sub_status_text",
                    "tracking_num",
                    "used_fund_subsidy"
                ],
                "properties": {
                    "activity_id": {
                        "type": "integer",
                        "title": "The activity_id schema"
                    },
                    "after_sign_redirect_link": {
                        "type": "string",
                        "title": "The after_sign_redirect_link schema"
                    },
                    "auto_sign": {
                        "type": "boolean",
                        "title": "The auto_sign schema"
                    },
                    "buy_again_link": {
                        "type": "string",
                        "title": "The buy_again_link schema"
                    },
                    "buy_prime_price": {
                        "type": "integer",
                        "title": "The buy_prime_price schema"
                    },
                    "buyer_address": {
                        "type": "object",
                        "title": "The buyer_address schema",
                        "required": [
                            "address_detail",
                            "city",
                            "city_id",
                            "district",
                            "district_id",
                            "id",
                            "province",
                            "province_id",
                            "receiver_name",
                            "receiver_tel",
                            "tag"
                        ],
                        "properties": {
                            "address_detail": {
                                "type": "string",
                                "title": "The address_detail schema"
                            },
                            "city": {
                                "type": "string",
                                "title": "The city schema"
                            },
                            "city_id": {
                                "type": "integer",
                                "title": "The city_id schema"
                            },
                            "district": {
                                "type": "string",
                                "title": "The district schema"
                            },
                            "district_id": {
                                "type": "integer",
                                "title": "The district_id schema"
                            },
                            "id": {
                                "type": "integer",
                                "title": "The id schema"
                            },
                            "province": {
                                "type": "string",
                                "title": "The province schema"
                            },
                            "province_id": {
                                "type": "integer",
                                "title": "The province_id schema"
                            },
                            "receiver_name": {
                                "type": "string",
                                "title": "The receiver_name schema"
                            },
                            "receiver_tel": {
                                "type": "string",
                                "title": "The receiver_tel schema"
                            },
                            "tag": {
                                "type": "string",
                                "title": "The tag schema"
                            }
                        }
                    },
                    "buyer_confirm_deadline": {
                        "type": "integer",
                        "title": "The buyer_confirm_deadline schema"
                    },
                    "buyer_confirm_delay_count": {
                        "type": "integer",
                        "title": "The buyer_confirm_delay_count schema"
                    },
                    "buyer_confirm_time": {
                        "type": "integer",
                        "title": "The buyer_confirm_time schema"
                    },
                    "can_add_review": {
                        "type": "integer",
                        "title": "The can_add_review schema"
                    },
                    "can_delay_sign": {
                        "type": "integer",
                        "title": "The can_delay_sign schema"
                    },
                    "can_urge_ship": {
                        "type": "integer",
                        "title": "The can_urge_ship schema"
                    },
                    "cancelable": {
                        "type": "integer",
                        "title": "The cancelable schema"
                    },
                    "compensation_service": {
                        "type": "array",
                        "title": "The compensation_service schema",
                        "items": {
                            "anyOf": [
                                {
                                    "type": "object",
                                    "title": "The first anyOf schema",
                                    "required": [
                                        "btn",
                                        "desc",
                                        "link",
                                        "title",
                                        "type"
                                    ],
                                    "properties": {
                                        "btn": {
                                            "type": "string",
                                            "title": "The btn schema"
                                        },
                                        "desc": {
                                            "type": "string",
                                            "title": "The desc schema"
                                        },
                                        "link": {
                                            "type": "string",
                                            "title": "The link schema"
                                        },
                                        "title": {
                                            "type": "string",
                                            "title": "The title schema"
                                        },
                                        "type": {
                                            "type": "integer",
                                            "title": "The type schema"
                                        }
                                    }
                                }
                            ]
                        }
                    },
                    "coupon_desc": {
                        "type": "string",
                        "title": "The coupon_desc schema"
                    },
                    "create_at": {
                        "type": "integer",
                        "title": "The create_at schema"
                    },
                    "credit_snap_id": {
                        "type": "string",
                        "title": "The credit_snap_id schema"
                    },
                    "evaluate_link": {
                        "type": "string",
                        "title": "The evaluate_link schema"
                    },
                    "express_name": {
                        "type": "string",
                        "title": "The express_name schema"
                    },
                    "finished_status": {
                        "type": "integer",
                        "title": "The finished_status schema"
                    },
                    "forbid_refund": {
                        "type": "boolean",
                        "title": "The forbid_refund schema"
                    },
                    "goods_desc": {
                        "type": "string",
                        "title": "The goods_desc schema"
                    },
                    "goods_group_id": {
                        "type": "integer",
                        "title": "The goods_group_id schema"
                    },
                    "goods_icon": {
                        "type": "string",
                        "title": "The goods_icon schema"
                    },
                    "goods_id": {
                        "type": "integer",
                        "title": "The goods_id schema"
                    },
                    "goods_link": {
                        "type": "string",
                        "title": "The goods_link schema"
                    },
                    "goods_name": {
                        "type": "string",
                        "title": "The goods_name schema"
                    },
                    "goods_quantity": {
                        "type": "integer",
                        "title": "The goods_quantity schema"
                    },
                    "goods_sku_id": {
                        "type": "integer",
                        "title": "The goods_sku_id schema"
                    },
                    "goods_snap_id": {
                        "type": "string",
                        "title": "The goods_snap_id schema"
                    },
                    "goods_specs": {
                        "type": "array",
                        "title": "The goods_specs schema",
                        "items": {
                            "anyOf": [
                                {
                                    "type": "object",
                                    "title": "The first anyOf schema",
                                    "required": [
                                        "spec_id",
                                        "spec_key",
                                        "spec_value"
                                    ],
                                    "properties": {
                                        "spec_id": {
                                            "type": "integer",
                                            "title": "The spec_id schema"
                                        },
                                        "spec_key": {
                                            "type": "string",
                                            "title": "The spec_key schema"
                                        },
                                        "spec_value": {
                                            "type": "string",
                                            "title": "The spec_value schema"
                                        }
                                    }
                                }
                            ]
                        }
                    },
                    "goods_unit_price": {
                        "type": "integer",
                        "title": "The goods_unit_price schema"
                    },
                    "group_order_id": {
                        "type": "string",
                        "title": "The group_order_id schema"
                    },
                    "id": {
                        "type": "string",
                        "title": "The id schema"
                    },
                    "is_evaluate": {
                        "type": "boolean",
                        "title": "The is_evaluate schema"
                    },
                    "latest_aftersale_status": {
                        "type": "integer",
                        "title": "The latest_aftersale_status schema"
                    },
                    "lock_status": {
                        "type": "integer",
                        "title": "The lock_status schema"
                    },
                    "logistic_id": {
                        "type": "integer",
                        "title": "The logistic_id schema"
                    },
                    "lucky_draw_id": {
                        "type": "integer",
                        "title": "The lucky_draw_id schema"
                    },
                    "mall_confirm_deadline": {
                        "type": "integer",
                        "title": "The mall_confirm_deadline schema"
                    },
                    "mall_confirm_time": {
                        "type": "integer",
                        "title": "The mall_confirm_time schema"
                    },
                    "mall_icon": {
                        "type": "string",
                        "title": "The mall_icon schema"
                    },
                    "mall_id": {
                        "type": "integer",
                        "title": "The mall_id schema"
                    },
                    "mall_name": {
                        "type": "string",
                        "title": "The mall_name schema"
                    },
                    "mall_tel": {
                        "type": "string",
                        "title": "The mall_tel schema"
                    },
                    "money_saved": {
                        "type": "string",
                        "title": "The money_saved schema"
                    },
                    "no_change_address": {
                        "type": "boolean",
                        "title": "The no_change_address schema"
                    },
                    "only_refund": {
                        "type": "boolean",
                        "title": "The only_refund schema"
                    },
                    "order_fund": {
                        "type": "array",
                        "title": "The order_fund schema",
                        "items": {}
                    },
                    "order_mall_icon": {
                        "type": "string",
                        "title": "The order_mall_icon schema"
                    },
                    "order_mall_link": {
                        "type": "string",
                        "title": "The order_mall_link schema"
                    },
                    "order_mall_name": {
                        "type": "string",
                        "title": "The order_mall_name schema"
                    },
                    "order_review_link": {
                        "type": "string",
                        "title": "The order_review_link schema"
                    },
                    "payment_activity_discount": {
                        "type": "integer",
                        "title": "The payment_activity_discount schema"
                    },
                    "payment_deadline": {
                        "type": "integer",
                        "title": "The payment_deadline schema"
                    },
                    "payment_express": {
                        "type": "integer",
                        "title": "The payment_express schema"
                    },
                    "payment_mall_discount": {
                        "type": "integer",
                        "title": "The payment_mall_discount schema"
                    },
                    "payment_method": {
                        "type": "integer",
                        "title": "The payment_method schema"
                    },
                    "payment_money_type": {
                        "type": "integer",
                        "title": "The payment_money_type schema"
                    },
                    "payment_order_id": {
                        "type": "string",
                        "title": "The payment_order_id schema"
                    },
                    "payment_status": {
                        "type": "integer",
                        "title": "The payment_status schema"
                    },
                    "payment_system_discount": {
                        "type": "integer",
                        "title": "The payment_system_discount schema"
                    },
                    "payment_time": {
                        "type": "integer",
                        "title": "The payment_time schema"
                    },
                    "payment_total": {
                        "type": "integer",
                        "title": "The payment_total schema"
                    },
                    "process_status": {
                        "type": "integer",
                        "title": "The process_status schema"
                    },
                    "recv_mobile": {
                        "type": "string",
                        "title": "The recv_mobile schema"
                    },
                    "recv_type": {
                        "type": "integer",
                        "title": "The recv_type schema"
                    },
                    "refund_id": {
                        "type": "string",
                        "title": "The refund_id schema"
                    },
                    "refund_status": {
                        "type": "integer",
                        "title": "The refund_status schema"
                    },
                    "refundable_amount": {
                        "type": "integer",
                        "title": "The refundable_amount schema"
                    },
                    "remark": {
                        "type": "string",
                        "title": "The remark schema"
                    },
                    "review_reward_coins": {
                        "type": "integer",
                        "title": "The review_reward_coins schema"
                    },
                    "ship_deadline": {
                        "type": "integer",
                        "title": "The ship_deadline schema"
                    },
                    "should_modify_real_name": {
                        "type": "boolean",
                        "title": "The should_modify_real_name schema"
                    },
                    "sign_reward_coins": {
                        "type": "integer",
                        "title": "The sign_reward_coins schema"
                    },
                    "status_text": {
                        "type": "string",
                        "title": "The status_text schema"
                    },
                    "sub_status_text": {
                        "type": "string",
                        "title": "The sub_status_text schema"
                    },
                    "tracking_num": {
                        "type": "string",
                        "title": "The tracking_num schema"
                    },
                    "used_fund_subsidy": {
                        "type": "integer",
                        "title": "The used_fund_subsidy schema"
                    }
                }
            },
            "time": {
                "type": "integer",
                "title": "The time schema"
            }
        }
    }
