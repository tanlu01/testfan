import os
from api.request import Request

class PayOrderQuery(Request):
    method = 'post'
    headers = {'Content-Type': 'application/json'}
    host = os.getenv('PAY_HOST')
    api = '/order/query'
    data = {
                "code": 0,
                "message": "",
                "currentTime": 1576500753,
                "data": {
                    "org_id": "",
                    "app_id": "bu2qpy6ejg9t",
                    "open_id": "",
                    "nonce_str": "9pqaDBzq5Az4ej1zjp4x0ymDKgQteB5v",
                    "order_no": "20191209194209427893004000000014",
                    "out_trade_no": "20191209194144-union-qtt-58041",
                    "amount": 100,
                    "title": "游戏中心",
                    "body": "游戏中心",
                    "code": 0,
                    "status": 5,
                    "channels": [
                        {
                            "id": 2,
                            "channel_id": 2,
                            "amount": 100,
                            "status": 4,
                            "voucher": "https://mclient.alipay.com/cashier/mobilepay.htm?alipay_exterface_invoke_assign_target=invoke_fc42fa06386e161f1cebdf3e3010f4a6&alipay_exterface_invoke_assign_sign=_r_m6_as_f_bz%2B7_j_pcn%2Bwu_p_yh_f_iz6_zhh_n_v_t_zjmf_v9s_a_pd_o_n_w_dlhs_lj_zc_e_z_q%3D%3D",
                            "err_msg": "",
                            "lock": 0,
                            "c_type": 0,
                            "tp_trade_no": ""
                        }
                    ]
                }
            }
    
    mock_status = 200
    mock_data = {
                    'code': 60000,
                    'message': 'from mock'
                }