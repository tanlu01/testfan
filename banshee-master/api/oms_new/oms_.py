import os
from api.request import Request
from jsonschema import validate


class Oms(Request):
    host = os.getenv('API_GATEWAY_OMS_HOST')
    headers = {'X-Token': ''}
    cookies = {}

    mock_status = 200
    mock_data = {
        'code': 60000,
        'message': 'from mock'
    }

    def request(self):
        resp = super().request()
        if hasattr(self, 'expected_schema'):
            validate(instance=resp, schema=self.expected_schema)
        return resp
