from api.oms_new.oms_ import Oms


class Create(Oms):
    method = 'post'
    api = '/omsapi/seckill/form'
    data = {
        "id": "",
        "activity_name": "秒杀活动测试",
        "act_time": [],
        "activity_step": 2,
        "extra.series": [],
        "schedule_id": 1208,
        "extra.exp_compensation_on": 0,
        "is_used": 0,
        "notify_emails": "",
        "sort_type": 1,
        "sort_strategy": 2100,
        "type": 8
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }


class AddSeries(Oms):
    method = 'post'
    api = '/omsapi/seckill/$activity_id/series'
    data = {
        "seckill_state": "2",
        "group_id": "486",
        "date": "2021-01-19"
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }


class GetSeries(Oms):
    method = 'get'
    api = '/omsapi/search/seckill/series'
    data = {
        "group_id": 488
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }


class GetGoodsDetail(Oms):
    method = 'get'
    api = '/omsapi/seckillgoods/$activity_id/list'
    data = {
        "_page": 1,
        "_size": 20
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }


class GoodsRelateSeries(Oms):
    method = 'post'
    api = '/omsapi/seckillgoods/$activity_id/destribute/batch'
    data = {
        'activity_id': 123,
        'selected': ''
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
