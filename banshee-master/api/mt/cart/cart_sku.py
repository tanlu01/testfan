from api.mt.mt import Mt
import os
import datetime
from random import randint


class CartSku(Mt):
    method = 'post'
    api = '/v1/cart/sku'
    data = {
        "extra": {
            "extra": {},
            "out_source": {
                "source_ref_pos_id": "shopping_cart.1",
                "ref_page_id": "goods_detail_1605863663135_jy6AhSmVsn",
                "ref_page_name": "goods_detail",
                "ref_key_param": "110436",
                "source_ref_page_id": "shopping_cart_1605863648690_RyQANxLoBV",
                "source_ref_page_name": "shopping_cart",
                "source_ref_key_param": ""
            }
        },
        "goods_id": "110436",
        "mall_id": 100241,
        "quantity": 1,
        "replace_sku_id": 0,
        "sku_id": 102311,
        "sku_price": 1,
        "sku_thumb_url": "http://qupinapptest.oss-cn-beijing.aliyuncs.com/1/202003/100241/CCCF9C4B77AA00CDDC3E2E7D53E9D5E7.jpg?x-oss-process=style/middle_p"
    }
    success_resp ={
        'code': 0
    }
    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }


    expected_schema = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "title": "expected_data",
        "type": "object",
        "required": ["code", "time", 'data'],
        "properties": {
            "code": {"type": "number"},
            "time": {"type": "number"},
            "data": {
                "type": "object",
                "required": ["delta"],
                "properties": {
                    "delta": {"type": "number"},
                }
            }
        }
    }
