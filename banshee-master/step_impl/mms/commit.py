from getgauge.python import step, data_store
from api.mms.products.commit import Commit
from api.mms.products.create_commit import CreateCommit
from models.mt.mt_goods_audit import Commit as CommitModel
import time


@step("获取创建商品的提交ID")
def creatcommit():
    creatcommit = CreateCommit()
    resp = creatcommit.request()
    assert resp['code'] == 0
    data_store.suite['commit_id'] = resp['payload']['commit_id']


@step("创建商品,商品价钱=<price>")
def commit(price):
    commit = Commit()
    commit.data['sku']['detail'][0]['normal_price'] = float(price)
    commit.data['sku']['detail'][0]['prime_price'] = float(price)
    commit.data['normal_price'] = float(price)
    commit.data['market_price'] = float(price)*100*2
    commit.data['id'] = data_store.suite['commit_id']
    commit.data['name'] = f"测试商品_{int(time.time())}"
    # print('\n商品名称：', commit.data['name'])

    resp = commit.request()
    assert resp['code'] == 0

    data_store.suite['goods_name'] = commit.data['name']
    data_store.suite['commit_goods_param'] = commit.data


@step("db更新商品待审核状态,mall_id=<mall_id>,goods_name=<goods_name>")
def update_audit_status(mall_id, goods_name):
    mall_id = data_store.suite['mall_id'] if not mall_id else mall_id
    goods_name = data_store.suite['goods_name'] if not goods_name else goods_name

    data = CommitModel.get(mall_id=mall_id, goods_name=goods_name)

    data_store.suite['commit_id'] = data.id
    data_store.suite['cat_id_2'] = data.cat_id_2
    data.audit_status = 17
    data.save()
