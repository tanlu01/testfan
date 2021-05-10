from api.oms_new.oms_ import Oms


class MallBalance(Oms):
    method = 'post'
    api = '/api/mall/Balance'
    data = {}

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

    expected_schema = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "title": "expected_data",
        "type": "object",
        "required": ["code", "payload"],
        "properties": {
            "code": {
                "type": "number"
            },
            "payload": {
                "type": "object",
                "required": ["id", "mall_id", "goods_payment_income", "goods_payment_expend", "shop_deposit_cash", "activity_deposit_cash", "activity_subsidy", "created_at", "update_at", "default_shop_deposit_cash", "goods_payment_withdrawing", "shop_deposit_withdrawing", "activity_deposit_withdrawing", "activity_subsidy_withdrawing", "goods_payment_freeze", "is_open", "loan_withdraw_times", "remain_withdraw_times", "activation_status", "sub_mch_state", "address", "need_annual_fee", "has_factory_info"],
                "properties": {
                    "id": {
                        "type": "string"
                    }, "mall_id": {
                        "type": "string"
                    }, "goods_payment_income": {
                        "type": "string"
                    }, "goods_payment_expend": {
                        "type": "string"
                    }, "shop_deposit_cash": {
                        "type": "string"
                    }, "activity_deposit_cash": {
                        "type": "string"
                    }, "activity_subsidy": {
                        "type": "string"
                    }, "created_at": {
                        "type": "string"
                    }, "update_at": {
                        "type": "string"
                    }, "default_shop_deposit_cash": {
                        "type": "string"
                    }, "goods_payment_withdrawing": {
                        "type": "string"
                    }, "shop_deposit_withdrawing": {
                        "type": "string"
                    }, "activity_deposit_withdrawing": {
                        "type": "string"
                    }, "activity_subsidy_withdrawing": {
                        "type": "string"
                    }, "goods_payment_freeze": {
                        "type": "string"
                    }, "is_open": {
                        "type": "string"
                    },
                    "punishment":{
                        "type": "object",
                        "required": [],
                        "properties": {}
                    },
                    "activity_forbidden":{
                        "type": "object",
                        "required": [],
                        "properties": {}
                    },
                    "loan_withdraw_times": {
                        "type": "number"
                    }, "remain_withdraw_times": {
                        "type": "number"
                    }, "activation_status": {
                        "type": "string"
                    }, "sub_mch_state": {
                        "type": "object",
                        "required": ["status", "info"],
                        "properties": {
                            "status": {
                                "type": "string"
                            },
                            "info": {
                                "type": "string"
                            },
                        }
                    }, "address": {
                        "type": "number"
                    }, "need_annual_fee": {
                        "type": "boolean"
                    }, "has_factory_info": {
                        "type": "boolean"
                    },
                }
            }
        }
    }
