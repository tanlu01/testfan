from getgauge.python import step, data_store
from api.oms.audit.audit import Audit
from models.mt.mt_goods_audit import Commit as CommitModel


@step("oms操作审核商品")
def audit():
    audit = Audit()
    audit.data['id'] = data_store.suite['commit_id']
    audit.data['old_leaf_cat_id'] = data_store.suite['cat_id_2']
    audit.data['goods_commit'] = data_store.suite['commit_goods_param']
    resp = audit.request()
    assert resp['code'] == 0


@step("获取商品ID并加入data_store")
def get_db_goods_id():
    mall_id = data_store.suite['mall_id']
    goods_name = data_store.suite['goods_name']

    data = CommitModel.get(mall_id=mall_id, goods_name=goods_name)
    data_store.suite['goods_id'] = data.goods_id
