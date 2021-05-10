# 前置条件：萌推APP登录，直购下单，预支付订单，发货，确认收货，申请售后

tags: app_pay, p0

## app login
* 萌推APP登录,通过手机号="15021721258"和验证码

## mms login并获取店铺基本信息
* MMS商家登录,通过用户名="18817300513",密码="12345678Zz"
* 获取商家店铺基本信息

## mms查看商品结算价
* mms查看商品结算价,goods_id="107807"

## oms login
* 新OMS小二后台登录,通过用户名="wenjie"和密码="a1a1a1"

## 领取平台优惠券
* 新OMS平台创建优惠券,参数:金额="6",门槛="20",适用范围类型="0_",领取限制="99",是否可领取=""

## 手动发券
* 手动发券,buyer_ids="",coupon_id=""

## 直购下单
* 直购下单,参数:商品id="107807",类目id="101658",支付方式="0",店铺优惠券id="ignore",平台优惠券id="",推币使用="ignore",礼品卡使用="ignore"

## mock支付订单
* 生成预支付订单并mock支付,order_id="",payment_method="",platform="50"

## mock支付后数据库检查
* mock支付后数据库检查,order_id=""


## MMS订单发货
* MMS订单发货,goods_id="",order_id=""


## 发货后数据库检查
* 发货成功后,订单表字段check,order_id=""
