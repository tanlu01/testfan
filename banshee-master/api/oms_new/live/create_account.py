from api.oms_new.oms_ import Oms


class CreateAccount(Oms):
    method = 'post'
    api = '/omsapi/live/account/form'
    data = {
        "id": "",
        "disabled": 0,
        "mobile": "15021721253",
        "company": "上海突进网络科技有限公司",
        "nickname": "小伍子",
        "avatar": "http://qupinapptest.oss-cn-beijing.aliyuncs.com/1/202012/e37e1f0d000f9965dba87c49cc5bea60.jpg",
        "realname": "伍义强",
        "passwd": "123456qq"
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
