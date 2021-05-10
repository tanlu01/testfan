# 前置条件：app登陆，商家登陆，萌推小二登陆, 商家新建商品，小二审核通过商品

tags: base00001, p0

## app login
* 萌推APP登录,通过手机号="15021721259"和验证码


## mms login并获取店铺基本信息
* MMS商家登录,通过用户名="18017752229",密码="19660302,.cj"

## mms创建商品
* 创建待审核商品,商品价钱="10",mall_id="",goods_name=""

## oms login
* OMS小二后台登录,通过手机号="wuyiqiang"和密码="1qaz2wsx!!"

## oms审核商品
* OMS审核商品

## 直购下单
* 直购下单,参数:商品id="",类目id="",支付方式="",店铺优惠券id="",平台优惠券id="",推币使用="",礼品卡使用=""

## mock支付订单
* 生成预支付订单并mock支付,order_id="",payment_method="",platform="50"

## MMS订单发货
* MMS订单发货,goods_id="",order_id=""

## 买家申请退款操作
* 买家申请退款操作,order_id="",refund_amount=""

## mock回调退款通知接口
* mock订单退款请求完成退款,order_id=""
