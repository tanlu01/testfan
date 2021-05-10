from api.request import Request
import os

class BatchIssue(Request):
    method = 'post'
    headers = {'Content-Type': 'application/json'}
    host = os.getenv('COUPON_HOST')
    api = '/coupon/v1/batchissue'
    data = {
        "users": [
            {
                "user_id": 192190049,
                "user_type": 1
            },
        ],
        "coupon_group_id": 1571745354971,
        "issue_source": "test",
        "token": "coupon"
    }

    mock_status = 200
    mock_data = {
                    'code': 60000,
                    'message': 'from mock'
                }