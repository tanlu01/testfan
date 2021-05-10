from api.oms_new.oms_ import Oms


class SystemCoupon(Oms):
    method = 'post'
    api = '/omsapi/coupon/form'
    data = {
        "id": "",
        "biz_title": "平台优惠券test",
        "type": 2,
        "scene_type": 15,
        "scene_text": "",
        "coupon_brand": "",
        "mall_id": "",
        "no_change": "",
        "amount": "6",
        "min_price": "20",
        "mall_amount": "0",
        "rule_id_type": 0,
        "rule_list_goods": "",
        "rule_list_category": "",
        "rule_list_act": "",
        "rule_list_special": "",
        "user_profile_type": 0,
        "get_time_absolute": [
          "2020-12-15 00:00",
          "2020-12-17 00:00"
        ],
        "use_relative": 0,
        "use_time_absolute": [
          "2020-12-15 00:00",
          "2020-12-17 00:00"
        ],
        "use_time_relative_day": 0,
        "use_time_relative_hour": 0,
        "count": "999999",
        "daily_limit": "9999",
        "per_user": "9999",
        "per_user_daily_limit": "",
        "need_alarm": 0,
        "alarm_threshold": 0,
        "alarm_receivers": [
          1
        ],
        "cannot_self_take": 0,
        "filter_type": 0,
        "filter_type_target": [

        ],
        "filter_type_group": "",
        "is_show": 0,
        "risk_strategy": 0,
        "rule_only_app": 0,
        "can_change_amount": 0,
        "purchase_coin": 0,
        "target_type": 0,
        "target_value_goods": "",
        "target_value_mall": "",
        "target_value_act": "",
        "target_value_channel": "",
        "target_value_h5link": "",
        "target_value_topicgroup": "",
        "sub_name": "全场通用",
        "status": "",
        "is_deleted": ""
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
            "message",
            "payload"
        ],
        "properties": {
            "code": {
                "type": "number"
            },
            "message": {
                "type": "string"
            },
            "payload": {
                "type": "object",
                }
        }
    }
