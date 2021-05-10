from getgauge.python import step, data_store
from api.mt.order.order_v1 import OrderV1
from api.mt.order.order_v2 import OrderV2
from api.mt.order.v1_order_check import OrderCheckV1
from api.mt.goods.address import Address, CreateAddress
from models.mt.mt_coupon import UserCoupon as UserCouponModel
import time


@step('获取收货地址id')
def address():
    address = Address()
    resp = address.request()
    assert resp['code'] == 0

    if not resp['data']['addrs']:
        create_address = CreateAddress()
        resp = create_address.request()
        assert resp['code'] == 0

        resp = address.request()
        assert resp['code'] == 0

    data_store.suite['address_id'] = resp['data']['addrs'][0]['address_id']


@step('支付前订单校验,商品id=<goods_id>,类目id=<sku_id>')
def order_check_v1(goods_id, sku_id):
    order_check_v1 = OrderCheckV1()

    order_check_v1.data['address_id'] = data_store.suite['address_id']
    order_check_v1.data['goods_id'] = data_store.suite['goods_id'] if not goods_id else int(goods_id)
    order_check_v1.data['goods_sku_id'] = data_store.suite['sku_info']['sku_id'] if not sku_id else int(sku_id)
    data_store.suite["order_sku_id"] = order_check_v1.data['goods_sku_id']

    times = 3
    while times > 0:
        try:
            resp = order_check_v1.request()
            assert resp['code'] == 0
        except Exception as e:
            print(e)
            time.sleep(5)
            times -= 1
        else:
            times = 0
    # 优惠种类：店铺优惠，平台优惠，推币，会员优惠，礼品卡
    data_store.suite['payment_total'] = resp['data']['order']['goods_unit_price']

    payment_mall_discount = resp['data']['order']['payment_mall_discount']
    if payment_mall_discount > 0:
        data_store.suite.setdefault('mall_coupon', {}).update({
            'id': resp['data']['owned_mall_coupon']['coupons'][0]['user_coupon_id'],
            'total': payment_mall_discount
        })
    else:
        data_store.suite.pop('mall_coupon', '')

    system_discount_detail = resp['data']['system_discount_detail']

    if system_discount_detail['system'] > 0:
        data_store.suite.setdefault('sys_coupon', {}).update({
            'id': resp['data']['owned_system_coupon']['coupons'][0]['user_coupon_id'],
            'total': system_discount_detail['system']
        })
    else:
        data_store.suite.pop('sys_coupon', '')

    if system_discount_detail['coin'] > 0:
        data_store.suite.setdefault('payment_coin', {}).update({
            'id': True,
            'total': system_discount_detail['coin']
        })
    else:
        data_store.suite.pop('payment_coin', '')

    if system_discount_detail['cash_card'] > 0:
        data_store.suite.setdefault('payment_cash_card', {}).update({
            'id': resp['data']['owned_cash_card']['cash_card'][0]['cash_card_id'],
            'total': system_discount_detail['cash_card']
        })
    else:
        data_store.suite.pop('payment_cash_card', '')

    if system_discount_detail['prime'] > 0:
        data_store.suite['prime_total'] = system_discount_detail['prime']
    else:
        data_store.suite.pop('prime_total', '')


# 以mall_coupon_id为例说明
# 如果传值为"",则默认从上下文获取
# 如果传值为具体id,则从数据库查询获取
# 如果不想使用,则传具体值：IGNORE
@step("直购下单,支付方式=<payment_method>,店铺优惠券id=<mall_coupon_id>,平台优惠券id=<sys_coupon_id>,推币使用=<coin>,礼品卡使用=<gift_card>")
def order_v1(payment_method, mall_coupon_id, sys_coupon_id, coin, gift_card):
    order_v1 = OrderV1()

    payment_method = data_store.suite.get('payment_method', 3) if not payment_method else payment_method
    user_id = data_store.suite['user_id']
    payment_total = data_store.suite['payment_total']

    check_dic = {'mall_coupon': mall_coupon_id, 'sys_coupon': sys_coupon_id, 'payment_coin': coin, 'payment_cash_card': gift_card}
    for key, value in check_dic.items():
        if value.strip().upper() == 'IGNORE':
            data_store.suite.pop(key, '')
        elif value:
            if key.endswith('coupon'):
                result = UserCouponModel.get(buyer_id=user_id, coupon_id=int(value))
                if len(result) == 1:
                    data_store.suite[key]['id'] = result.id
                    payment_total -= result.amount
        elif not value:
            payment_total -= data_store.suite.get(key, {}).get('total', 0)

    payment_total -= data_store.suite['prime_total'] if data_store.suite.get('prime_total', False) else 0
    mall_coupon_id = data_store.suite.get('mall_coupon', {}).get('id', '')
    sys_coupon_id = data_store.suite.get('sys_coupon', {}).get('id', '')
    cash_card_id = data_store.suite.get('payment_cash_card', {}).get('id', '')
    use_coins = data_store.suite.get('payment_coin', {}).get('id', False)

    order_v1.data['coupon_id'].clear()
    order_v1.data['selected_cash_card'].clear()
    order_v1.data['address_id'] = data_store.suite['address_id']
    order_v1.data['goods_id'] = int(data_store.suite['goods_id'])
    order_v1.data['goods_sku_id'] = int(data_store.suite['sku_info']['sku_id'])
    order_v1.data['payment_method'] = int(payment_method)
    order_v1.data['expected_payment_total'] = payment_total
    order_v1.data['coupon_id'].append(str(mall_coupon_id)) if mall_coupon_id else ''
    order_v1.data['coupon_id'].append(str(sys_coupon_id)) if sys_coupon_id else ''
    order_v1.data['selected_cash_card'].append(str(cash_card_id)) if cash_card_id else ''
    order_v1.data['use_coins'] = use_coins
    order_v1.data['selected_mall_coupon_id'] = str(mall_coupon_id) if mall_coupon_id else ''
    order_v1.data['selected_system_coupon_id'] = str(sys_coupon_id) if sys_coupon_id else ''

    resp = order_v1.request()
    print('订单信息', resp)
    assert resp['code'] == 0
    assert resp['data']['order_id'] != ''

    data_store.suite['order_id'] = resp['data']['order_id']
    data_store.suite['payment_method'] = order_v1.data['payment_method']
    data_store.suite['payment_total'] = order_v1.data['expected_payment_total']


@step("购物车下单, mall_id=<mall_id>,goods_id=<goods_id>,goods_sku_id=<goods_sku_id>,expected_unit_price=<expected_unit_price>,payment_method=<payment_method>")
def order_v2(mall_id, goods_id, goods_sku_id, expected_unit_price, payment_method):
    order_v2 = OrderV2()
    order_v2.data['order_items'][0]['mall_id'] = data_store.spec["mall_id"] if not mall_id else int(mall_id)
    order_v2.data['order_items'][0]['order_goods'][0]['goods_id'] = int(goods_id)
    order_v2.data['order_items'][0]['order_goods'][0]['goods_sku_id'] = data_store.spec["sku_id"] if not goods_sku_id else int(goods_sku_id)
    order_v2.data['order_items'][0]['order_goods'][0]['expected_unit_price'] = int(expected_unit_price)
    order_v2.data['payment_method'] = int(payment_method)
    order_v2.data['expected_payment_total'] = int(expected_unit_price)
    resp = order_v2.request()
    assert resp['code'] == 0
    order_id=resp["data"]["order_id"]
    data_store.suite["order_id"]=order_id
    data_store.suite["union_order_id"]=order_id[6:]

