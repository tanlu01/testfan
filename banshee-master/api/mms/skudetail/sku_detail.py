from api.mms.mms_ import Mms


class SkuDetail(Mms):
    method = 'get'
    api = '/api/goods/getSkuDetail?goods_id=107807'
    data = {
        "goods_id":"107807"
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
        "payload"
      ],
      "properties": {
        "code": {
          "type": "number"
        },
        "payload": {
          "type": "object",
          "required": [
            "sku",
            "spec",
            "lock"
          ],
          "properties": {
            "sku":{
                "type":"array",
                "items":{
                    "type":'object',
                    "properties":{
                        'sku_id':{'type':'string'},
                        'goods_id':{'type':'string'},
                        'normal_price':{'type':'string'},
                        'cost':{'type':'string'}
                    }
                }
            },
            "spec":{
                "type":"object",
                "required":["spec_one"],
                "properties":{
                    "spec_one":{
                        "type":'string'
                    }
                }
            },
            "lock":{
                "type":"object",
                "required":["disable_edit_specification","disable_take_down_spu","disable_take_down_sku","disable_edit_cost_template","disable_prolong_pre_sale_time","disable_add_sku_price","disable_reduce_sku_price","disable_reduce_stock"],
                "properties":{
                    "disable_edit_specification":{"type":'boolean'},
                    "disable_take_down_spu":{"type":'boolean'},
                    "disable_take_down_sku":{"type":'boolean'},
                    "disable_edit_cost_template":{"type":'boolean'},
                    "disable_prolong_pre_sale_time":{"type":'boolean'},
                    "disable_add_sku_price":{"type":'boolean'},
                    "disable_reduce_sku_price":{"type":'boolean'},
                    "disable_reduce_stock":{"type":'boolean'}
                }
            }
          }
        }
      }
    }


