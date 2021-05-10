import os, uuid, time, random, string
from api.request import Request
from api.encrypt import member_data_encrypt
from api.encrypt import account_sign

class Member(Request):
    public_params = {
        # 反作弊
        'tk': 'ACELOPU2FhaHVoi7m2VG' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(24)),
        # 早期的设备码，不敏感
        'distinct_id': '4ae0d3520d74d804',
        # 早期的设备码，不敏感
        'deviceCode': '866777030562869',
        # 客户端的version
        'version': '30910000',
        # android version
        'OSVersion': '7.0',
        # 投放渠道
        'dtu': '01',
        # 经纬度
        'lat': '0.0',
        'lon': '0.0',
        # 不敏感
        'network': 'wifi',
        'time': int(time.time()*1000),
        'uuid': uuid.uuid4().hex,
        # 客户端的小版本号
        'versionName': '3.9.10.000.0201.1532'
    }

    def request(self):
        encrypted_data = member_data_encrypt(self.data)
        self.data.clear()
        self.data['qdata'] = encrypted_data
        return super().request()


class Passport(Request):
    public_params = {
        "app_id": "Qukan.zhibo",
        "app_version": "30910000",
        "app_version_name": "3.9.10.000.0201.1532",
        "os": "android",
        "os_version": "7.0",
        "tk": "ACELOPU2FhaHVoi7m2VGa9C7SDGNjkEigZMUvzQ0BLKu",
        "deviceCode": "866777030562868",
        "network": "wift",
        "uuid": uuid.uuid4().hex,
        "time": int(time.time()),
        "ip": '2001:0db8:85a3:0000:0000:8a2e:0370:0218'
    }

    def request(self):
        sign = account_sign(
            params=self.data['public_params'], ingnored_keys=(), filter_falsy=False)
        self.data['public_params']['sign'] = sign
        return super().request()
