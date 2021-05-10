from getgauge.python import step, data_store
from api.lego.projects.create import Create, AddItems, SaveItems, PublishItems
from time import time
import hashlib


@step("创建乐高项目")
def projects_create():
    projects_create = Create()

    now = int(time()*1000)
    projects_create.data['project_name'] = f'测试项目_{now}'
    projects_create.data['start_time'] = now
    projects_create.data['end_time'] = now + 86400000

    resp = projects_create.request()

    assert resp['code'] == 0
    #print('新建项目名称：', projects_create.data['project_name'])
    data_store.suite['lego_project_id'] = resp['data']['id']


# code: marketing_coupon, goods_waterfall
@step("新增乐高项目组件,项目id=<project_id>,组件code=<item_code>")
def add_items(project_id, item_code):
    add_items = AddItems()

    add_items.data['page_id'] = data_store.suite['lego_project_id'] if not project_id else int(project_id)
    add_items.data['brick_type_code'] = item_code
    resp = add_items.request()
    assert resp['code'] == 0

    data_store.suite[item_code] = resp['data']['id']


@step('保存乐高项目,标题=<title>')
def save_items(title):
    save_items = SaveItems()

    save_items.data['conf']['config']['title']['text'] = title if title else f'测试项目_{int(time()*1000)}'

    for brick in save_items.data['bricks']:
        if brick['brick_type'] == 'marketing_coupon':
            brick['config']['items'][0]['target_val'] = data_store.suite['coupon_id']
            brick['config']['items'][0]['target_text'] = f"{data_store.suite['coupon_id']} | {data_store.suite['coupon_desc']}"
            brick['id'] = data_store.suite['marketing_coupon']
            brick['config']['sign'] = hashlib.md5((data_store.suite['coupon_id']+'qingfeng_1212').encode('utf8')).hexdigest()
        elif brick['brick_type'] == 'goods_waterfall':
            brick['config']['items'][0]['target_val'] = data_store.suite['activity_id']
            brick['config']['items'][0]['target_text'] = data_store.suite['activity_desc']
            brick['id'] = data_store.suite['goods_waterfall']

    save_items.api = save_items.api.replace('$project_id', f"{data_store.suite['lego_project_id']}")
    resp = save_items.request()

    assert resp['code'] == 0


@step('发布乐高项目')
def publish_items():
    publish_items = PublishItems()

    publish_items.api = publish_items.api.replace('$project_id', f"{data_store.suite['lego_project_id']}")
    resp = publish_items.request()

    assert resp['code'] == 0
