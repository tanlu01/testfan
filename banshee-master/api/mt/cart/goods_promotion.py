from api.mt.mt import Mt


class Goods_promotion(Mt):
    method = 'post'
    api = '/v1/cart/goods_promotion'
    data = {
        "goods_id": "107893",
        "mall_id": 100005,
        "promotion_id": "",
        "sku_id": 101749
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
                "required": ["mall_goods", "mall_id"],
                "properties": {
                    "mall_goods": {
                        "type": "array",
                        'items': {
                            'type': 'object',
                            'properties': {}
                        }
                    },
                    "mall_id": {"type": "number"}
                }
            }
        }
    }

