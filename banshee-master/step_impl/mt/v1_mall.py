from getgauge.python import step, data_store
from api.mt.mt import Mt
from api.mt.mall.coupons import Coupons
from api.mt.mall.detail import Detail
from api.mt.mall.info import V1_mall_info
from api.mt.mall.qualification import Qualification


@step("获取当前店铺所有优惠券, mall_id=<mall_id>")
def coupons(mall_id):
    coupons = Coupons()
    coupons.api = coupons.api.replace("$mall_id", mall_id)
    coupons.request()
    print(coupons.resp.json())


@step("店铺详情, mall_id=<mall_id>")
def detail(mall_id):
    detail = Detail()
    detail.api = detail.api.replace("$mall_id", mall_id)
    detail.request()
    print(detail.resp.json())


@step("店铺信息, mall_id=<mall_id>")
def V1_mall_info(mall_id):
    info = V1_mall_info()
    info.api = info.api.replace("$mall_id", mall_id)
    info.request()
    print(info.resp.json())


@step("店铺资质, mall_id=<mall_id>")
def qualification(mall_id):
    qualification = Qualification()
    qualification.api = qualification.api.replace("$mall_id", mall_id)
    qualification.request()
    print(qualification.resp.json())
    # 无法获取到图片验证码暂时