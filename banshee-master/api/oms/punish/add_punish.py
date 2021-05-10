from api.oms.oms_ import Oms


class Add_punish(Oms):
    method = 'post'
    api = '/mallpunishmentrecord/addOrEdit'
    data = {
        "id":0,
        "mall_id":0,
        "open_time": "",
        "detail": "",
        "rule_id": "",
        "score": 0,
        "money": 0,
        "limit": 0,
        "limit_name": "活动报名",
        "limit_days": 1,
        "punishment_detail": "",
        "related_order":"",
        "related_sku":"",
        "images": [],
        "status": "",
        "appeal_detail":"",
        "handle_detail":"",
        "handle_text": "",
        "update_at": "",
        "punish_at":"",
        "mall_name":""
    }
    success_resp = {
        'code': 0,
    }
    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }