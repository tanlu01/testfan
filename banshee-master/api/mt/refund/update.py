from api.mt.mt import Mt
import os
import datetime
from random import randint


class Update(Mt):
    method = 'post'
    api = '/v1/refund/$refund_id/update'
    data = {
        "operator_type": 1, # 1-买家,2-买家,3-小二
        "mobile_num": "15021721254",  # 退款人联系电话
        "refund_amount": 0,  # 退款金额
        "reason_id": 5,  # 售后原因id
        "refund_type": 0,  # 退款id，仅更新退款信息时需要
        "received": 1,  # 是否已收到货(1:未收到货;2:已收到货)
        "tag_ids": [17, 18, 19],
        "remark_text": "",
        "remark_imgs": []
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
