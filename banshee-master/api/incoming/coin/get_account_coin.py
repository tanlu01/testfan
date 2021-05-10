from api.request import Request
import os

class GetAccountCoin(Request):
    method = 'get'
    headers = {'Content-Type': 'application/json'}
    host = os.getenv('COIN_HOST')
    api = '/account/getAccountCoin'
    data = {
        "user_id": 747583
    }

    mock_status = 200
    mock_data = {
                    'code': 60000,
                    'message': 'from mock'
                }