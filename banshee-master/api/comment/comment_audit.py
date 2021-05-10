from api.oms_new.oms_ import Oms


class Comment_audit(Oms):
    method = 'post'
    api = '/omsapi/comment/audit'
    data = {
        "id":1000097105,
        "audit_status":2,
        "reason_id":1,
        "other_reason":""
        }

    success_resp = {
        'code': 0
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
