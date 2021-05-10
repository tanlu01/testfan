from api.mt.mt import Mt


class Address(Mt):
    method = 'get'
    api = '/v1/users/addresses'
    data = {}

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }


class CreateAddress(Mt):
    method = 'post'
    api = '/v1/users/addresses'
    data = {
        "address": "申江路5005弄星创科技广场1号楼",
        "city_id": 321,
        "country_id": 1,
        "district_id": 2707,
        "is_default": True,
        "mobile": "15021721254",
        "name": "测试人",
        "province_id": 25,
        "tag": ""
    }

    success_resp = {
        'code': 0
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
