import os, time, json
from api.incoming.incoming import Incoming


class CouponPay(Incoming):
    method = 'post'
    headers = {'Content-Type': 'application/json'}
    host = os.getenv('INCOMING_GATEWAY_HOST')
    api = '/coupon/v4/pay'
    data = {
        "pay": Incoming.pay,
        # "coupon": Incoming.coupon,
        "total_fee": 100,
        "user_type": 13,
        "third_part_id": 0,
        "new_coin": 1389,
        "is_subaccount": False,
        "timestamp": int(time.time()*1000),
        "token": 'e72eY0vAIRVbKid2oY7qLpl9L2FRz3nsreuAe-pDQZJSkpNti5Y5HwjqAMaNOee_J3keC5t_3p8FHq205z42-qivvh5nWwF2MAhToF8KmMCikJKMdXI'
    }

    mock_status = 200
    mock_data = {
        'code': 60000,
        'message': 'from mock'
    }
