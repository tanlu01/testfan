import operator, random, string, logging
from api.mt.user.login import Login
from api.mt.mt import Mt

def launch_loading(obj, params, is_catch_response=True):
    _set_xtoken_to_headers(obj.x_token, params['headers'])

    with operator.methodcaller(params['method'], params['api'], headers = params['headers'], json = params['data'], catch_response=is_catch_response)(obj.client) as resp:
        if resp.json()['code'] == 0:
            resp.success()
        else:
            resp.failure(f"response 'code' should be 0. {resp.json()}")

def mt_login(mobile = False):
    login = Login()
    login.data['mobile'] = mobile if mobile else '130' + ''.join(random.choice(string.digits) for _ in range(8))
    resp = login.request()
    return resp['data']['token']

def _set_xtoken_to_headers(x_token, headers):
    headers['X-Token'] = x_token

