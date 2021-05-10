from api.mms.mms_ import Mms
import time


class Commit(Mms):
    method = 'post'
    api = '/api/goods/commit'
    data = {"spec_tpl_id": 3,
            "is_new": "1",
            "name": f"测试商品_{int(time.time())}",
            "brand_id": "147",
            "footnote": "test_footnote",
            "second_hand_goods": "0",
            "type": "0",
            "event_type": "1",
            "is_pre_sale": "0",
            "shipment_limit_second": 172800,
            "is_refundable": "1",
            "is_original_auth": "1",
            "thumb_url": "",
            "ethumb_url": "",
            "detail_pics": ["oss/1/202008/E37E1F0D000F9965DBA87C49CC5BEA60.jpg"],
            "image_url": "oss/1/202008/27699DC3C2DA386C91A2619A1DA6BF5F.jpg",
            "carousel_pics": ["oss/1/202008/E37E1F0D000F9965DBA87C49CC5BEA60.jpg"],
            "video_id": "",
            "video_url": "",
            "features": "[]",
            "cat_id": ["10031", "10034"],
            "goods_desc_json": [],
            "weight": "0",
            "sku": {
                "spec_type": 3,
                "spec_one": 3,
                "spec_two": 4,
                "spec_one_sub": [2538],
                "spec_two_sub": [175],
                "detail": [
                    {
                        "stock": 1,
                        "normal_price": 0.01,
                        "out_sku_sn": "",
                        "thumb_url": "oss/1/202008/E37E1F0D000F9965DBA87C49CC5BEA60.jpg",
                        "is_onsale": "1",
                        "cost": 0,
                        "prime_price": 0.01,
                        "bar_codes": [],
                        "type": 0,
                        "key": "2538175",
                        "spec_one_sub":2538,
                        "spec_one_sub_remark":"",
                        "spec_two_sub":175,
                        "spec_two_sub_remark":""
                    }
                ]
            },
            "market_price": 2,
            "normal_price": 0.01,
            "total_stock": 1,
            "out_goods_sn": "",
            "single_meta": {"buy_limit": 9999, "order_limit": 9999},
            "biz": {
                "expiration_date": '',
                "produced_date": ['', ''],
                "product_licence": '',
                "product_standard_num": '',
                "goods_images": ["oss/1/202008/E37E1F0D000F9965DBA87C49CC5BEA60.jpg"]
            },
            "is_onsale": "1",
            "goods_tags": {},
            "brands": [],
            "cost_template_id": "259",
            "food_safety": {"quality_guarantee_period": ''},
            "mz_qualification": {
                "expired_at": '',
                "approval_at": '',
                "filing_certification_pic": [

                ],
                "ex_factory_certificate": [

                ]
            },
            "brand_name": "test/测试",
            "custom_specs": [],
            "use_new_tpl": 1,
            "id": "100005506",
            "is_pulish": True
            }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
