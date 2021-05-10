from api.mt.mt import Mt

class Experience_prime(Mt):
    method = 'post'
    api = '/v1/prime/free_buy'
    data = {
            "type": 1,
            "page_name": "{\"ref_page_name\":\"goods_detail\",\"ref_key_param\":\"37645213\",\"page_name\":\"prime.prime_free\",\"page_id\":\"x.prime.prime_free_1609162241863_T9Q0Mzk4fU\",\"ref_page_id\":\"goods_detail_1609162232846_MTmgpfLN89\",\"mode\":\"receive_free_prime\",\"from_pos\":\"goods_detail_bar_free_prime\"}",
            "platform": 50
    }
    success_resp ={
        'code':0
    }
    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
