from getgauge.python import step, data_store
import os, string, random, responses
from datetime import datetime, timedelta
from models.incoming.pay import TbCouponGroupBaseInfo
from api.incoming.coupon.save_coupon_group import SaveCouponGroup
from api.incoming.coupon.batch_issue import BatchIssue
from api.incoming.coin.get_account_coin import GetAccountCoin
from api.incoming.coin.new_coin import NewCoin
from api.incoming.order.create import Create

@step("创建并获取券批次, user_id = <user_id>, app_id = <app_id>")
def create_coupon_group_by_user_and_app(user_id, app_id):
    data_store.scenario["user_id"] = int(user_id)
    data_store.scenario["app_id"] = app_id

    save_coupon_group = SaveCouponGroup()
    save_coupon_group.data['coupon_group_name'] = '测试券库' + ''.join(random.choice(string.ascii_letters) for _ in range(12))
    save_coupon_group.data['total_stock_num'] = 10
    save_coupon_group.data['user_type'] = 1
    save_coupon_group.data['app_id'] = data_store.scenario["app_id"]
    save_coupon_group.data['use_rule_type'] = 1
    save_coupon_group.data['product_ids'] = [os.getenv('PRODUCT_ID')]
    save_coupon_group.data['coupon_type'] = 1
    save_coupon_group.data['start_time'] = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
    save_coupon_group.data['end_time'] = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')

    resp = save_coupon_group.request()
    row = TbCouponGroupBaseInfo.get(TbCouponGroupBaseInfo.coupon_group_id == resp['data']['coupon_group_id'])

    data_store.scenario["coupon_group_id"] = resp['data']['coupon_group_id']
    data_store.scenario["price_limit"] = save_coupon_group.data['price_limit']
    
    assert resp['code'] == 0
    assert resp['message'] == 'success'
    assert row.status == 1
    assert row.coupon_group_id == resp['data']['coupon_group_id']
    assert row.coupon_group_name == save_coupon_group.data['coupon_group_name']

@step("给用户添加券")
def add_coupon_to_user():
    batch_issue = BatchIssue()
    batch_issue.data['coupon_group_id'] = data_store.scenario["coupon_group_id"]
    batch_issue.data['users'][0]['user_id'] = data_store.scenario["user_id"]

    resp = batch_issue.request()
    
    data_store.scenario["coupon_code"] = resp['data']['couponbatchissueinfo']['issued_coupons'][0]['coupon_code']
    data_store.scenario["user_type"] = batch_issue.data['users'][0]['user_type']

    assert resp['code'] == 0
    assert resp['message'] == 'success'

@step("查询主账号的金币余额, coins = <coins>")
def query_account_coins(coins):
    get_account_coin = GetAccountCoin()
    get_account_coin.data['user_id'] = data_store.scenario["user_id"]
    resp = get_account_coin.request()
    
    data_store.scenario['coins'] = resp['data']['coins']

    assert resp['code'] == 0

@step("给主账号充值, amount = <amount>")
def charging_coins_to_user(amount):
    data_store.scenario['amount'] = int(amount)

    new_coin = NewCoin()
    new_coin.data['amount'] = data_store.scenario['amount']
    new_coin.data['user_id'] = data_store.scenario["user_id"]
    new_coin.data['op_user_id'] = data_store.scenario["user_id"]
    resp = new_coin.request()

    assert resp['code'] == 0

@step("下单判断该用户是否作弊, code = <code>")
# @responses.activate
def check_user_cheating_or_not(code):
    create = Create()
    create.data['mock_status'] = 500
    create.data['user_id'] = data_store.scenario["user_id"]
    create.data['user_type'] = data_store.scenario["user_type"]
    create.data['coupon']['code'] = data_store.scenario["coupon_code"]
    create.data['app_id'] = data_store.scenario["app_id"]
    create.data['coin']['new_coin'] = data_store.scenario['coins']
    create.data['coin']['is_sub_account'] = False
    create.data['product']['price'] = int(data_store.scenario["price_limit"] + data_store.scenario['coins']/100 + 1)
    resp = create.request()
    assert resp['code'] == int(code)

