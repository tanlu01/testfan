from getgauge.python import step, data_store
from api.oms_new.coupon.system_coupon import SystemCoupon
from api.oms_new.coupon.coupon_list import CouponList
from api.oms_new.coupon.audit import Audit
from api.oms_new.coupon.coupon_give import CouponGive
import datetime
from datetime import date, timedelta
import time
from models.mt.mt_coupon import UserCoupon as UserCouponModel


# 适用范围类型，参数传值参考: 1_123,如果不需要传值:1_
# {value: 0, label: "全场通用"}
# {value: 1, label: "部分商品适用"}
# {value: 2, label: "部分类目适用"}
# {value: 5, label: "全场通用-除虚拟商品外"}
# {value: 6, label: "部分专题适用"}
# {value: 7, label: "部分商品适用(仅限虚拟商品)"}
# 领取限制:优惠券总数_每日库存_每人限领: 100_10_1
# 是否可领取: 不可领取:1,全部用户领取:0
@step("新oms新建平台优惠券,金额=<amount>,门槛=<min_price>,适用范围类型=<rule_info>,领取限制=<select_limit>,是否可领取=<select_check>")
def system_coupon(amount, min_price, rule_info, select_limit, select_check):
    rule_list = {
        0: None,
        1: 'rule_list_goods',
        2: 'rule_list_category',
        5: None,
        6: 'rule_list_special',
        7: 'rule_list_goods'
    }
    system_coupon = SystemCoupon()

    if rule_info:
        type, value = rule_info.split('_')
        if int(type) not in rule_list:
            raise Exception(f'rule_info参数传值不正确,参考值:{list(rule_list.keys())},格式1_123')
        else:
            system_coupon.data['rule_id_type'] = int(type)
            rule_list_value = rule_list[int(type)]
            system_coupon.data[rule_list_value] = [int(i) for i in value.split(',')] if rule_list_value and value else data_store.suite.get('activity_id', '')

    cur1 = datetime.datetime.now() 
    cur2 = cur1 + datetime.timedelta(days=1)

    if select_limit:
        select_data = select_limit.split('_')
        data_store.suite.setdefault('select_data', {}).update(dict(zip(['count', 'daily_limit', 'per_user'], select_data)))
    if select_check:
        data_store.suite['cannot_self_take'] = int(select_check)

    system_coupon.data['biz_title'] = f"平台优惠券测试_{str(time.time())}"
    system_coupon.data['get_time_absolute'] = [str(cur1), str(cur2)]
    system_coupon.data['use_time_absolute'] = [str(cur1), str(cur2)]
    system_coupon.data['amount'] = int(amount) if amount else 5
    system_coupon.data['min_price'] = int(min_price) if min_price else 10
    system_coupon.data['count'] = data_store.suite.get('select_data', {}).get('count', 100)
    system_coupon.data['daily_limit'] = data_store.suite.get('select_data', {}).get('daily_limit', 10)
    system_coupon.data['per_user'] = data_store.suite.get('select_data', {}).get('per_user', 1)
    system_coupon.data['cannot_self_take'] = data_store.suite.get('cannot_self_take', 0)
    resp = system_coupon.request()

    assert resp['code'] == 0
    data_store.suite['coupon_name'] = system_coupon.data['biz_title']
    data_store.suite['coupon_desc'] = f'满{min_price}减{amount}'


@step("获取平台优惠券列表")
def couponlist():
    curmin = date.today()
    curmax = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    couponlist = CouponList()
    couponlist.api = couponlist.api.replace('$create_at1', str(curmin)).replace('$create_at2', str(curmax))

    resp = couponlist.request()

    assert resp['code'] == 0

    flag = False
    for coupon_info in resp['payload']['list']:
        if coupon_info['biz_title'] == data_store.suite['coupon_name']:
            data_store.suite['coupon_id'] = resp['payload']['list'][0]['id']
            #print('新建优惠券id:', data_store.suite['coupon_id'])
            flag = True
            break
    assert flag


@step("平台优惠券审核,优惠券id=<coupon_id>")
def audit(coupon_id):
    coupon_id = data_store.suite['coupon_id'] if not coupon_id else coupon_id
    audit = Audit()
    audit.api = audit.api.replace("$coupon_id", coupon_id)
    resp = audit.request()

    assert resp['code'] == 0


@step("手动发券,buyer_ids=<buyer_ids>,coupon_id=<coupon_id>")
def coupongive(buyer_ids, coupon_id):
   buyer_ids = data_store.suite['user_id'] if not buyer_ids else buyer_ids
   coupon_id = data_store.suite['coupon_id'] if not coupon_id else coupon_id
   
   coupongive =CouponGive()
   coupongive.data['buyer_ids'] = buyer_ids
   coupongive.data['coupon_id'] = coupon_id
   resp = coupongive.request()

   assert resp['code'] == 0


@step("获取用户发放的优惠券id")
def get_coupon_id():
    user_coupon = UserCouponModel.get(coupon_id=data_store.suite['coupon_id'])
    data_store.suite['coupon_id'] =user_coupon.id
    print(data_store.suite['coupon_id'])
