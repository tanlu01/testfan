import os
from api.request import Request
from jsonschema import validate
from tools.redis_mixin import RedisMixin


class Mms(RedisMixin, Request):
    host = os.getenv('API_GATEWAY_MMS_HOST')
    headers = {
        'Content-Type': 'application/json',
        'Cookie': '',
    }
    cookies = {}

    mock_status = 200
    mock_data = {
        'code': 60000,
        'message': 'from mock'
    }

    def __init__(self):
        self.redis_connect = {
            'host': os.getenv('MMS_REDIS_HOST'),
            'password': os.getenv('MMS_REDIS_PSW'),
            'port': int(os.getenv('MMS_REDIS_PORT')),
            'db': int(os.getenv('MMS_REDIS_DB')),
            'decode_responses': True
        }

    def request(self):
        resp = super().request()
        if hasattr(self, 'expected_schema'):
            validate(instance=resp, schema=self.expected_schema)
        return resp
