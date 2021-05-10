from getgauge.python import step, data_store
from api.act.seckill.create import Create, GoodsDetail, ApplyGoods, VerifyGoods
from models.mt.mt_apply import Application as ApplicationModel
import uuid
import datetime


@step("创建秒杀活动")
def create():
    create = Create()

    schedule = datetime.datetime.now()
    start = schedule.strftime("%Y-%m-%d %H:%M:%S")
    end = (schedule + datetime.timedelta(days=2)).strftime("%Y-%m-%d")

    create.data['name'] = f'秒杀报名_{str(uuid.uuid4())[-10:]}'
    create.data['apply_start_time'] = start
    create.data['apply_end_time'] = end
    create.data['schedule_start_time'] = start
    create.data['schedule_end_time'] = end

    resp = create.request()
    assert resp['code'] == 0
    data_store.suite['act_seckill_activity_id'] = resp['payload']['id']
    print('秒杀活动ID:', resp['payload']['id'])


@step("获取待添加活动的商品详情,商品id=<goods_id>")
def goods_detail(goods_id):
    goods_id = data_store.suite['goods_id'] if not goods_id else goods_id

    goods_detail = GoodsDetail()
    goods_detail.api = goods_detail.api.replace('$goods_id', str(goods_id))

    resp = goods_detail.request()
    assert resp['code'] == 0
    data = resp['payload']
    data.pop('skus_title')

    skus = data['skus'][0]

    data['sku_info'] = [skus]
    data['skus'] = [skus]
    data['stock'] = skus['stock']

    data_store.suite['seckill_goods_info'] = data


@step("活动添加商品")
def apply_goods():
    apply_goods = ApplyGoods()

    apply_goods.data['promotion_goods_info'].update(data_store.suite['seckill_goods_info'])

    normal_price = float(data_store.suite['seckill_goods_info']['skus'][0]['normal_price'])
    update_price = {
        'activity_cost': normal_price*0.9,
        'price': normal_price+5,
        'activity_stock': data_store.suite['seckill_goods_info']['stock'],
        '_checked': True
    }

    apply_goods.data['promotion_goods_info']['skus'][0].update(update_price)
    apply_goods.data['promotion_goods_info']['sku_info'][0].update(update_price)
    apply_goods.data['promotion_goods_info']['activity_stock'] = data_store.suite['seckill_goods_info']['stock']
    apply_goods.data['goods_id'] = str(data_store.suite['seckill_goods_info']['goods_id'])
    apply_goods.data['schedule_id'] = str(data_store.suite['act_seckill_activity_id'])
    resp = apply_goods.request()

    assert resp['code'] == 0


@step("审核商品,活动id=<activity_id>")
def verify_goods(activity_id):
    verify_goods = VerifyGoods()

    activity_id = data_store.suite['act_seckill_activity_id'] if not activity_id else activity_id

    application = ApplicationModel()
    data = application.filter(schedule_id=activity_id)

    goods_ids = [i.id for i in data]
    code = {'pass_first': '通过', 'pass_second': '复审通过'}

    for goods_id in goods_ids:
        verify_goods.api = verify_goods.api.replace('$goods_id', str(goods_id))

        for key, value in code.items():
            verify_goods.data['_action']['code'] = key
            verify_goods.data['_action']['text'] = value

            resp = verify_goods.request()

            assert resp['code'] == 0
