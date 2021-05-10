from api.mt.mt import Mt


class Profile_prime(Mt):
    method = "get"
    api = "/v1/prime/profile"
    data = {

    }
    success_resp = {
        "code": 0
    }
    error_resp = {
        "code": 40000, "message": "没有可购买的商品"
    }
