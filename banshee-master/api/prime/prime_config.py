from api.mt.mt import Mt


class Prime_config(Mt):
    method="get"
    api="/v2/prime/home/config?is_home=1"
    data={}
    success_resp={
        "code":0
    }
    error_resp={
        'code': 400000,
        'message': '没有可以购买的商品'
    }
