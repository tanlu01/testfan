from api.mt.mt import Mt
import os
import datetime
from random import randint


class V2_Detail(Mt):
    method = 'get'
    api = '/v2/order/union_order/$order_id/detail'
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
                    "create_at",
                    "buyer_address",
                    "recv_mobile",
                    "payment_deadline",
                    "payment_money_type",
                    "payment_method",
                    "payment_status",
                    "money_saved",
                    "payment_time",
                    "status_text",
                    "sub_status_text",
                    "top_hint",
                    "pt_discount",
                    "mall_discount",
                    "payment_total",
                    "payment_express",
                    "process_status",
                    "coupon_desc",
                    "list",
                    "payment_order_id",
                    "no_change_address",
                    "no_pay_order_alert",
                    "order_mall_name",
                    "order_mall_icon",
                    "order_mall_link",
                    "buy_again_link",
                    "goods_link",
                    "is_evaluate",
                    "evaluate_link",
                    "lock_status",
                    "buy_prime_price",
                    "order_fund"
                ],
                "properties": {
                    "id": {
                        "type": "string"
                    },
                    "create_at": {
                        "type": "number"
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
                    "payment_deadline": {
                        "type": "number"
                    },
                    "payment_money_type": {
                        "type": "number"
                    },
                    "payment_method": {
                        "type": "number"
                    },
                    "payment_status": {
                        "type": "number"
                    },
                    "money_saved": {
                        "type": "string"
                    },
                    "payment_time": {
                        "type": "number"
                    },
                    "status_text": {
                        "type": "string"
                    },
                    "sub_status_text": {
                        "type": "string"
                    },
                    "top_hint": {
                        "type": "string"
                    },
                    "pt_discount": {
                        "type": "number"
                    },
                    "mall_discount": {
                        "type": "number"
                    },
                    "payment_total": {
                        "type": "number"
                    },
                    "payment_express": {
                        "type": "number"
                    },
                    "process_status": {
                        "type": "number"
                    },
                    "coupon_desc": {
                        "type": "string"
                    },
                    "list": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "mall_id": {
                                    "type": "number"
                                },
                                "mall_name": {
                                    "type": "string"
                                },
                                "mall_icon": {
                                    "type": "string"
                                },
                                "mall_tel": {
                                    "type": "string"
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
                                "coupon_desc": {
                                    "type": "string"
                                },
                                "goods": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
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
                                            "should_modify_real_name": {
                                                "type": "boolean"
                                            }
                                        }
                                    }
                                },
                                "remark": {
                                    "type": "string"
                                }
                            }
                        }
                    },
                    "payment_order_id": {
                        "type": "string"
                    },
                    "no_change_address": {
                        "type": "boolean"
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
                    "goods_link": {
                        "type": "string"
                    },
                    "is_evaluate": {
                        "type": "boolean"
                    },
                    "evaluate_link": {
                        "type": "string"
                    },
                    "lock_status": {
                        "type": "number"
                    },
                    "buy_prime_price": {
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
