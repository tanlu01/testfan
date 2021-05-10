from getgauge.python import step, data_store
from api.oms_new.activity.seckill import Create, AddSeries, GetSeries, GetGoodsDetail, GoodsRelateSeries
from models.mt.pt_activity import ActivityGroup as AGModel
import datetime


@step("新小二后台创建秒杀活动,新报名系统秒杀报名id=<seckill_id>")
def create(seckill_id):
    create = Create()

    schedule = datetime.datetime.now()

    now = schedule.strftime("%Y-%m-%d")
    end = (schedule+datetime.timedelta(days=2)).strftime("%Y-%m-%d")
    series_start = schedule.strftime("%H:%M")
    series_end = (schedule+datetime.timedelta(hours=2)).strftime('%H:%M')

    create.data['act_time'].extend([f'{now} 00:00:00', f'{end} 00:00:00'])
    create.data['schedule_id'] = data_store.suite['act_seckill_activity_id'] if not seckill_id else int(seckill_id)
    create.data['extra.series'].extend([{'start_time': series_start}, {'start_time': series_end}])
    resp = create.request()
    assert resp['code'] == 0


@step("根据秒杀报名ID从db获取秒杀活动ID,新报名系统秒杀报名id=<seckill_id>")
def get_oms_new_activity_id(seckill_id):
    seckill_id = data_store.suite['act_seckill_activity_id'] if not seckill_id else seckill_id
    data = AGModel.get(schedule_id=int(seckill_id))
    data_store.suite['oms_new_activity_id'] = data.id
    print('OMS秒杀活动ID', data.id)


@step("新增活动档期,秒杀活动id=<activity_id>")
def add_series(activity_id):
    activity_id = data_store.suite['oms_new_activity_id'] if not activity_id else activity_id

    add_series = AddSeries()

    add_series.api = add_series.api.replace('$activity_id', str(activity_id))
    add_series.data['group_id'] = str(activity_id)
    add_series.data['date'] = datetime.datetime.now().strftime('%Y-%m-%d')

    resp = add_series.request()
    assert resp['code'] == 0


@step("获取活动档期,秒杀活动id=<activity_id>")
def get_series(activity_id):
    activity_id = data_store.suite['oms_new_activity_id'] if not activity_id else activity_id

    get_series = GetSeries()

    get_series.data['group_id'] = int(activity_id)

    resp = get_series.request()

    assert resp['code'] == 0

    data = sorted(resp['payload'], key=lambda key: key['value'])
    data_store.suite['series_id'] = data[0]['value']


@step("获取活动关联的商品信息,秒杀活动id=<activity_id>")
def get_goods_detail(activity_id):
    activity_id = data_store.suite['oms_new_activity_id'] if not activity_id else activity_id

    get_goods_detail = GetGoodsDetail()
    get_goods_detail.api = get_goods_detail.api.replace('$activity_id', str(activity_id))

    resp = get_goods_detail.request()

    assert resp['code'] == 0

    data_store.suite['activity_goods_detail'] = resp['payload']['list']


@step("设置商品关联活动档期,秒杀活动id=<activity_id>,档期id=<series_id>")
def goods_relate_series(activity_id, series_id):
    activity_id = data_store.suite['oms_new_activity_id'] if not activity_id else activity_id
    series_id = data_store.suite['series_id'] if not series_id else series_id

    goods_relate_series = GoodsRelateSeries()
    goods_relate_series.api = goods_relate_series.api.replace('$activity_id', str(activity_id))

    goods_relate_series.data['selected'] = data_store.suite['activity_goods_detail']
    goods_relate_series.data['activity_id'] = str(series_id)

    resp = goods_relate_series.request()
    assert resp['code'] == 0

