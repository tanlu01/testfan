import jwt
import time


def generate_token():
    now = int(time.time())
    data = {
        'iat': now,
        'exp': now + 24 * 3600,
        'user_info': {
            'id': 10000,
            'name': '蜗壳',
            'alias_name': '蜗壳',
            'email': '',
            'avatar': 'https://static-legacy.dingtalk.com/media/lADPD3zULsdguVTNAnHNAnE_625_625.jpg',
            'mobile': '18516001568',
        }
    }

    key = 'mt-jwt'
    headers = {
        'alg': 'HS256',
        'typ': 'JWT',
    }

    return jwt.encode(data, key, algorithm='HS256', headers=headers)
