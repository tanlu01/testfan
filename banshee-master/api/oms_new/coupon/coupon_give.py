from api.oms_new.oms_ import Oms
import datetime



class CouponGive(Oms):
    method = 'post'
    api = '/omsapi/coupongive/form'
    data = {
        "id":"",
        "buyer_ids":"36020943",
        "coupon_id":"8572389985806761984",
        "remark":"333"
    }
  
    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

{
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
      "required": [
        
      ],
      "properties": {
        
      }
    }
  }
}