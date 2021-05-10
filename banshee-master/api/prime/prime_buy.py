from api.mt.mt import Mt

class Prime_buy(Mt):
    method = 'post'
    api = '/v1/prime/buy'
    data = {
        "page_name":"",
        "master_invite_code": "",
        "payment_method": 3,
        "platform": 50,
        "stage": "",
        "scene": "",
        "package_id": ""
}
    success_resp ={
        'code':0
    }
    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
