import os, time, hashlib, json, base64, redis

def _sign(func):
    def wrapper_sign(*args, **kwargs):
        sorted_list = []
        for param in sorted(kwargs['params'].items()):
            if param[0] in kwargs['ingnored_keys']: continue
            if kwargs['filter_falsy']: 
                if not param[1]: continue
            v = json.dumps(param[1]) if isinstance(param[1], dict) else param[1]
            sorted_list.append(f"{param[0]}={v}")
        sorted_list.append(func(*args, **kwargs))
        sorted_str = '&'.join(sorted_list)
        return hashlib.md5(sorted_str.encode()).hexdigest()
    return wrapper_sign

@_sign
def account_sign(*args, **kwargs):
    key = os.getenv('ACCOUNT_ENCRYPTION_KEY')
    return f'key={key}'

@_sign
def incoming_sign(*args, **kwargs):
    key = os.getenv('INCOMING_ENCRYPTION_KEY')
    timestamp = kwargs['params']['timestamp']
    token = kwargs['params']['token']
    return f'secret={key}{timestamp}{token}'

def member_data_encrypt(data):
    r = redis.Redis(host=os.getenv("ACCOUNT_REDIS_HOST"), port=os.getenv("ACCOUNT_REDIS_PORT"))
    if int(data['dtu']) == 200:
        encrypt = r.hget('encrypt', 'h5.' + str('ab28c644-bc00-4f41-b34a-5a0e4f7410d1') + '.' + json.dumps(data))
    elif 100 <= int(data['dtu']) < 300 :
        encrypt = r.hget('encrypt', 'ios.' + str('ab28c644-bc00-4f41-b34a-5a0e4f7410d2') + '.' + json.dumps(data))
    else:
        encrypt = r.hget('encrypt', 'android.' + str('ab28c644-bc00-4f41-b34a-5a0e4f7410d9') + '.' + json.dumps(data))
    return base64.b64encode(encrypt).decode()
