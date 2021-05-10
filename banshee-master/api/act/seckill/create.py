from api.act.act_ import Act


class Create(Act):
    method = 'post'
    api = '/api/sp/v1/apply/schedules'
    data = {
        "type": 6,
        "act_rules": {
            "mall_cost": "",
            "data": [],
            "pay_type": 1
        },
        "thumb": "1/sp/202101/d4830164_c79e_4d0f_87bd_c645ef35ed1a.jpg",
        "name": "秒杀报名",
        "desc": "简介",
        "module_type_id": 12,
        "apply_start_time": "2021-01-15 10:19:57",
        "apply_end_time": "2021-01-16 00:00:00",
        "schedule_start_time": "2021-01-15 10:19:57",
        "schedule_end_time": "2021-01-16 00:00:00",
        "rule": "<p>说明</p>",
        "act_type": 1,
        "sub_type": 1,
        "apply_requirement": {
            "mall_filter_type": 0,
            "mall_ids": "",
            "mall_types": [],
            "staple_ids": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
            "mall_tip": [],
            "join_days_range": {"min": "", "max": ""},
            "mall_score_staple": [],
            "buyer_satisfaction_180days_staple": [],
            "avg_shipping_rating_30days_staple": [],
            "avg_aftersale_rating_30days_staple": [],
            "avg_service_rating_30days_staple": [],
            "cat_ids": [],
            "sales_requirement": [],
            "activity_image_type": [],
            "brand_types": [],
            "pre_sale_time": [],
            "history_min_normal_price_days": "",
            "price_range": {"min": "", "max": ""},
            "activity_price_range": {"min": "", "max": ""},
            "discount_rate": {"min": "", "max": ""},
            "prime_price_rate": "",
            "ref_coupons": 0,
            "coupon_conf": [
                {
                    "min_price": "",
                    "discount_amount": "",
                    "mall_cost": ""
                }
            ],
            "cost": {"min": "", "max": ""},
            "activity_cost": {"min": "", "max": ""},
            "mall_display": 1,
            "price_lock": 0,
            "value_or_stock": 1,
            "min_value": "",
            "activity_stock": "",
            "activity_stock_range": {"min": "", "max": ""},
            "free_region": [],
            "goods_review": [],
            "buyer_total_limit_range": {"min": "", "max": ""},
            "buyer_limit_range": {"min": "", "max": ""},
            "apply_count_condition_type": 2,
            "max_apply_num": "",
            "audit_pass_rate": [
                {
                    "label": "[0% ~ 30%)",
                    "max_rate": "30",
                    "max_apply_num": ""
                },
                {
                    "label": "[30% ~ 50%)",
                    "max_rate": "50",
                    "max_apply_num": ""
                },
                {
                    "label": "[50% ~ 80%)",
                    "max_rate": "80",
                    "max_apply_num": ""
                },
                {
                    "label": "[80% ~ 100%]",
                    "max_rate": "100",
                    "max_apply_num": ""
                }
            ],
            "max_apply_count_condition": {
                "days": "",
                "min_sales": "",
                "max_apply_num": ""
            },
            "increase_apply_count_condition": {
                "days": "",
                "sales": "",
                "mul_apply_num": ""
            },
            "gmv_eliminated_threshold": 10,
            "act_type": 1,
            "sub_type": 1,
            "activity_tag": []
        }
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }


class GoodsDetail(Act):
    method = 'get'
    api = '/api/sp/v1/goods/$goods_id'
    data = {}

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }


class ApplyGoods(Act):
    method = 'post'
    api = '/api/sp/v1/applications'
    data = {
        "goods_id": "107808",
        "schedule_id": "1185",
        "promotion_goods_info": {
            "goods_id": "107808",
            "name": "test",
            "thumb_url": "1/201912/100241/CCCF9C4B77AA00CDDC3E2E7D53E9D5E7.jpg",
            "image_url": "",
            "footnote": "test",
            "market_price": 6000,
            "unit_order_limit": 9999,
            "buyer_total_limit_range": 9999,
            "extension_from": 0,
            "is_onsale": 1,
            "mall_id": 100241,
            "single_meta": {
                "buy_limit": 9999,
                "order_limit": 9999,
                "single_unity_limit": 9999,
                "single_buyer_number_limit": 9999
            },
            "goods_name": "test",
            "stock": 99907,
            "skus": [],
            "skus_title": [
                {
                    "type": "selection",
                    "__id": "NaXQZv"
                },
                {
                    "key": "thumb_url",
                    "title": "缩略图",
                    "slot": "thumb_url",
                    "__id": "t0dIbU"
                },
                {
                    "key": "sku_id",
                    "title": "skuid",
                    "__id": "3BkVv7"
                },
                {
                    "key": "cost",
                    "title": "结算价",
                    "__id": "uOpVl7"
                },
                {
                    "title": "活动结算价",
                    "slot": "activity_cost",
                    "width": "105px",
                    "__id": "LDGbrH"
                },
                {
                    "key": "normal_price",
                    "title": "售价",
                    "__id": "x90GaL"
                },
                {
                    "title": "活动价",
                    "slot": "price",
                    "width": "105px",
                    "__id": "pzhFRg"
                },
                {
                    "key": "prime_price",
                    "title": "会员价",
                    "__id": "K3pzRh"
                },
                {
                    "key": "stock",
                    "title": "线上库存",
                    "__id": "WpdX3e"
                },
                {
                    "title": "活动库存",
                    "slot": "activity_stock",
                    "width": "105px",
                    "__id": "vlcXH9"
                }
            ],
            "can_edit": False,
            "activity_stock": 99907,
            "sku_info": []
        }
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }


class VerifyGoods(Act):
    method = 'put'
    api = '/api/sp/v1/applications/$goods_id'
    data = {
        "_action": {
            "code": "pass_first",
            "text": "通过",
            "payload": None
        }
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
