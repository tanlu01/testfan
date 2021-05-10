from api.request import Request
import os

class InfoProductid(Request):
    method = 'get'
    headers = {'Content-Type': 'application/json'}
    host = os.getenv('BUSINESS_MONITOR_HOST')
    api = '/info/productid'
    data = {}

    mock_status = 200
    mock_data = {
                    'code': 60000,
                    'message': 'from mock'
                }
                