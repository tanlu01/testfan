from api.oms_new.oms_ import Oms


class Audit(Oms):
    method = 'post'
    api = '/omsapi/coupon/audit/$coupon_id'
    data = {
        "remark": "",
        "pass": 0,
        "action": 1
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
          "required": [

          ],
          "properties": {

          }
        }
      }
    }