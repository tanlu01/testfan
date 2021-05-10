from api.mt.mt import Mt
import os
import datetime
from random import randint


class Order_check(Mt):
    method = 'post'
    api = '/v2/order_check'
    data = {
        "payment_method": 3,
        "payment_money_type": 0,
        "pt_coupon_id": "0",
        "auto_select_system_coupon": True,
        "auto_select_cash_card": True,
        "selected_cash_card": [],
        "type": 1,
        "order_items": [{
            "auto_select_mall_coupon": True,
            "mall_id": 100003,
            "coupon_id": "0",
            "order_goods": [{
                "expected_unit_price": 1200,
                "goods_id": 12008,
                "goods_quantity": 1,
                "goods_sku_id": 67600,
                "ext_data": {
                    "mall_id": 100003,
                    "sku": {
                        "sku_id": 67600,
                        "thumb_url": "http://qupinapptest.oss-cn-beijing.aliyuncs.com/1/201801/6c865e02c7bfb58c13cef120d0d011a4.jpeg?x-oss-process=style/middle",
                        "quantity": 1,
                        "is_onsale": True,
                        "normal_price": 1200,
                        "group_price": 1200,
                        "cc": 0,
                        "spec_combo": "1097,12887",
                        "specs": [{
                            "spec_id": 1097,
                            "spec_key": "尺码",
                            "spec_value": "XXXXL"
                        }, {
                            "spec_id": 12887,
                            "spec_key": "颜色",
                            "spec_value": "黑色连衣裙"
                        }],
                        "extra": {
                            "extra": {},
                            "out_source": {
                                "ref_page_id": "goods_detail_1611027474838_lAE2mBSDGm",
                                "ref_page_name": "goods_detail",
                                "source_ref_key_param": "",
                                "source_ref_page_id": "shopping_cart_1611027473035_sECi8KCqaw",
                                "source_ref_pos_id": "shopping_cart.1",
                                "source_ref_page_name": "shopping_cart",
                                "ref_key_param": "12008",
                                "activity_id": 0
                            }
                        }
                    },
                    "goods_name": "12008【S码—4XL码】【80斤—180斤可穿】",
                    "thumb_url": "http://qupinapptest.oss-cn-beijing.aliyuncs.com/1/201801/6c865e02c7bfb58c13cef120d0d011a4.jpeg?x-oss-process=style/middle",
                    "goods_unit_price": 1200,
                    "service_promise_mark": [{
                        "id": "mn_exp_compensation",
                        "text": "贵必赔",
                        "style": 301,
                        "name": "exp_compensation",
                        "img_url": "http://file.mengtuiapp.com/1/biz/fcs9R0kyxqjK-1585634693334.png",
                        "img_ratio": "3.786"
                    }, {
                        "id": "cat_service",
                        "text": "差必赔",
                        "style": 202,
                        "name": "bad_compensation",
                        "img_url": "http://file.mengtuiapp.com/1/biz/fm4UpbOYLbrd-1585634951295.png",
                        "img_ratio": "3.786"
                    }, {
                        "id": "cat_service",
                        "text": "假一赔四",
                        "style": 201,
                        "name": "origin_auth",
                        "img_url": "http://file.mengtuiapp.com/1/biz/EzGBTHVyufM0-1590379245886.png",
                        "img_ratio": "3.571"
                    }, {
                        "id": "cat_service",
                        "text": "7天无理由退换",
                        "style": 201,
                        "name": "refundable",
                        "img_url": "http://file.mengtuiapp.com/1/biz/l48I7N1tnWzt-1585636304303.png",
                        "img_ratio": "5.643"
                    }],
                    "out_source": {
                        "ref_page_id": "goods_detail_1611027474838_lAE2mBSDGm",
                        "ref_page_name": "goods_detail",
                        "source_ref_key_param": "",
                        "source_ref_page_id": "shopping_cart_1611027473035_sECi8KCqaw",
                        "source_ref_pos_id": "shopping_cart.1",
                        "source_ref_page_name": "shopping_cart",
                        "ref_key_param": "12008",
                        "activity_id": 0
                    }
                }
            }]
        }],
        "address_id": 345394,
        "auto_select_coins": False,
        "use_coins": False,
        "system_promotion_id": "",
        "last_selected_type": 0,
        "no_select_system_promotion": False
}


    success_resp={
        "code":0
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
