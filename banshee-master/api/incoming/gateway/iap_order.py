import os
from api.incoming.incoming import Incoming


class IapOrder(Incoming):
    method = 'post'
    headers = {'Content-Type': 'application/json'}
    host = os.getenv('INCOMING_GATEWAY_HOST')
    api = '/iap/v1/order'
    data = {
        "token": '9f55vPuNBrKRP_n_5UZAFlSgxcRn9brziJZ-UDcwM36m2YKhlOHucSRKAVzvGBJkzBEMQytfGNy1rQ7ABpCJfBnbkN_1ZzeDnXcHQbEIzyypIVXmSgA',
        "app_id": '1',
        "product": '11111',
        # "user_type": 1,
        # "out_order_no": '',
        # "extra": '',
        "pay": Incoming.pay
    }

    mock_status = 200
    mock_data = {
        'code': 60000,
        'message': 'from mock'
    }
