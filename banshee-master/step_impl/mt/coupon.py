from getgauge.python import step, data_store
from api.mt.v2_mall.coupons import DetailLegoProject, ReceiveCoupon
from models.mt.mt_coupon import Coupon as CouponModel


@step("获取乐高项目优惠券详情页,项目id=<lego_project_id>")
def detail_lego_project(lego_project_id):
    detail_lego_project = DetailLegoProject()
    detail_lego_project.data['project_id'] = data_store.suite['lego_project_id'] if not lego_project_id else int(lego_project_id)

    resp = detail_lego_project.request()

    assert resp['code'] == 0


@step("用户领取优惠券,券id=<coupon_id>")
def receive_coupon(coupon_id):
    coupon_id = data_store.suite['coupon_id'] if not coupon_id else coupon_id

    coupon_data = CouponModel.get(id=int(coupon_id))

    receive_coupon = ReceiveCoupon()
    receive_coupon.data['coupon_id'] = coupon_id

    for _ in range(coupon_data.per_user):
        resp = receive_coupon.request()
        assert resp['code'] == 0
        assert resp['data']['toast_msg'] == '领取成功'
    else:
        resp = receive_coupon.request()
        assert resp['code'] == 0
        assert resp['data']['toast_msg'] == '当前用户领取该券数量已达上限'
