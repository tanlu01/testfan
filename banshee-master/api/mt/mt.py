import os
import uuid
import time
import random
import string
from api.request import Request
from jsonschema import validate


class Mt(Request):
    host = os.getenv('API_GATEWAY_HOST')
    headers = {
        'Content-Type': 'application/json',
        'X-Token': '7975emeQA2KSVylZPGqF17NDIn0TJ4d6rscQKPNX3fak319k0xtuYp1j2Z9DkBb9oR_2t1NWt_rkv00Vc6Y9xhbd9iG5oO2YM_6ZtOgvxzmgjIh-e2c',
        'x-device': 'QUNKYXBiNGZhSWxFNlk5bFZVY0g5LUs3ZGpORXAyY1R5SHB0Wlc1bmRIVnB8OGY5MDgwMjdiZWYxNDBjZTM4Njc1NTBlMTdiMGY3YWQxYWU2ZmJmYw==',
        'x-tk': 'ACJapb4faIlE6Y9lVUcH9-K7djNEp2cTyHptZW5ndHVp',
        'x-ver': '2.9.8',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MengTuiApp/2.9.8 X-Feature/fund_returns,prime'
    }
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