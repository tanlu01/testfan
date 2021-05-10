import os
from api.incoming.incoming import Incoming


class IapVerify(Incoming):
    method = 'post'
    headers = {'Content-Type': 'application/json'}
    host = os.getenv('INCOMING_GATEWAY_HOST')
    api = '/iap/v1/verify'
    data = {
        "order_no": 'bu2qpy6ejg9t',
        "transaction_id": "9pqaDBzq5Az4ej1zjp4x0ymDKgQteB5v",
        "receipt_data": '20191209194209427893004000000014'
    }

    mock_status = 200
    mock_data = {
        'code': 60000,
        'message': 'from mock'
    }
