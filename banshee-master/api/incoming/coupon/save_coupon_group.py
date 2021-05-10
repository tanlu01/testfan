from api.request import Request
import os

class SaveCouponGroup(Request):
    method = 'post'
    headers = {'Content-Type': 'application/json'}
    host = os.getenv('COUPON_HOST')
    api = '/coupon/v1/savecopongroup'
    data = {
        "coupon_group_name": "测试券库0726-pre",
        "start_time": "2019-07-10 06:53:25",  # 开始时间
        "end_time": "2019-08-10 07:57:48",  # 结束时间
        "coupon_value": 50,  # 券面额
        "price_limit": 100,  # 券门槛
        "coupon_type": 1,  # 1 - 满减券 2 折扣券
        "total_stock_num": 2,  # 总库存
        "use_rule_type": 1,  # 1 - 全场通用，2 - 需要校验商品
        "app_id": "bt8dot25xwfc",  # 渠道id  bt8dot25xwfc 直播  测试环境  bteevncrky5n  线上环境 btat0kfof36u 米读
        "max_per_user": 10,  # 个人最大领取次数
        "instruction": "qute auto test create coupon group",  # 介绍
        "memo": "qute auto test",
        "effective_days": 14,  # n天内可用，最后一天23: 59:59
        "user_type": 1,  # 用户类型1 - qtt，2 - 米读
        "add_user": "qute auto tester",
        "update_user": "qute auto tester",
        "product_ids": ['a3y64cDEpArW'],  # 商品id的list
        "discount_value": 88 ,# 折扣 1 ~ 99 之间的数值，表示折扣。eg: 80 表示 80 / 100 = 8 折
        "max_deduct_price": 100 # 折扣券最大抵扣金额（分）
    }

    mock_status = 200
    mock_data = {
                    'code': 60000,
                    'message': 'from mock'
                }